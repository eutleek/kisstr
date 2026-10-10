# -*- coding: utf-8 -*-
"""Kisstr 一键上传脚本（Neocities API）
用法：python upload_neocities.py
按提示输入 Neocities 用户名和密码（不会保存），自动递归上传：
  index.html -> 根目录
  html/*    -> /html/
  assets/*  -> /assets/
  wallpapers/* -> /wallpapers/
  thumbs/*  -> /thumbs/
保留目录结构，分批上传（每批 25 个文件）。
"""
import os
import sys
import getpass
import json
import urllib.request
import urllib.parse
import uuid

ROOT = os.path.dirname(os.path.abspath(__file__))
API = "https://neocities.org/api/upload"
BATCH = 25

def collect():
    """收集 (远程路径, 本地路径)"""
    items = []
    root_idx = os.path.join(ROOT, "index.html")
    if os.path.exists(root_idx):
        items.append(("index.html", root_idx))
    for sub in ["html", "assets", "wallpapers", "thumbs"]:
        base = os.path.join(ROOT, sub)
        if not os.path.isdir(base):
            continue
        for dirpath, _, files in os.walk(base):
            rel = os.path.relpath(dirpath, ROOT).replace("\\", "/")
            for f in sorted(files):
                remote = (rel + "/" + f) if rel != "." else f
                items.append((remote, os.path.join(dirpath, f)))
    return items

def upload_batch(user, passwd, batch):
    boundary = "----KisstrUpload" + uuid.uuid4().hex
    body = []
    for remote, local in batch:
        with open(local, "rb") as fh:
            data = fh.read()
        body.append(("--" + boundary).encode())
        body.append(('Content-Disposition: form-data; name="%s"; filename="%s"\r\nContent-Type: application/octet-stream\r\n\r\n' % (remote, remote)).encode("utf-8"))
        body.append(data)
        body.append(b"\r\n")
    body.append(("--" + boundary + "--\r\n").encode())
    payload = b"".join(body)

    req = urllib.request.Request(API, data=payload, method="POST")
    req.add_header("Content-Type", "multipart/form-data; boundary=" + boundary)
    req.add_header("Content-Length", str(len(payload)))
    import base64
    token = base64.b64encode((user + ":" + passwd).encode("utf-8")).decode("ascii")
    req.add_header("Authorization", "Basic " + token)

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            out = resp.read().decode("utf-8", "replace")
            return json.loads(out)
    except urllib.error.HTTPError as e:
        return {"result": "error", "err": e.code, "msg": e.read().decode("utf-8", "replace")[:300]}

def delete_file(user, passwd, remote_path):
    """删除 Neocities 上的文件（如旧 html/index.html）"""
    import base64
    body = urllib.parse.urlencode({"filenames[]": remote_path}).encode("utf-8")
    req = urllib.request.Request("https://neocities.org/api/delete", data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    token = base64.b64encode((user + ":" + passwd).encode("utf-8")).decode("ascii")
    req.add_header("Authorization", "Basic " + token)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        return {"result": "error", "err": e.code, "msg": e.read().decode("utf-8", "replace")[:200]}

def main():
    if sys.version_info[0] < 3:
        print("需要 Python 3")
        return
    items = collect()
    print("共 %d 个文件待上传（index.html + html/assets/wallpapers/thumbs）" % len(items))
    if not items:
        print("未找到文件，请确认脚本放在项目根目录（与 html/、wallpapers/ 同级）")
        return
    user = input("Neocities 用户名: ").strip()
    passwd = getpass.getpass("Neocities 密码: ")

    # 清理旧的 html/index.html（主页已移回根目录，避免重复入口）
    r = delete_file(user, passwd, "html/index.html")
    print("清理旧 html/index.html:", "success" if r.get("result") == "success" else r.get("msg", r))

    ok = fail = 0
    for i in range(0, len(items), BATCH):
        batch = items[i:i + BATCH]
        r = upload_batch(user, passwd, batch)
        if r.get("result") == "success":
            ok += len(batch)
            print("[%d/%d] 成功 %d 个" % (i + len(batch), len(items), len(batch)))
        else:
            fail += len(batch)
            print("[失败] %s %s" % (r.get("err"), r.get("msg")))
            print(" 批次文件:", [b[0] for b in batch[:5]])
    print("完成：成功 %d，失败 %d" % (ok, fail))
    print("访问 https://eutleek.neocities.org/ 验证")

if __name__ == "__main__":
    main()
