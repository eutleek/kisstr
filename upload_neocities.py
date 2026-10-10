# -*- coding: utf-8 -*-
"""
Kisstr 站点上传脚本（Neocities API）
结构：site/ 为上传根目录（HTML 平铺 + wallpapers/ + thumbs/ + robots.txt）
上传时 site/ 内容平铺到 Neocities 根：kisstr.com/xxx.html
用法：python upload_neocities.py
"""
import sys, os, json, getpass, urllib.request, urllib.parse, base64

BATCH = 25
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# 旧结构残留（html/ 目录、assets/ 目录），上传前清理
LEGACY_CLEAN = []
def build_legacy_clean():
    html_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")
    if os.path.isdir(html_dir):
        for f in os.listdir(html_dir):
            if f.endswith(".html"):
                LEGACY_CLEAN.append("html/" + f)
    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
    if os.path.isdir(assets_dir):
        for f in os.listdir(assets_dir):
            LEGACY_CLEAN.append("assets/" + f)

def collect():
    items = []
    def add(rel, path):
        if os.path.isfile(path):
            items.append((rel, path))
    if os.path.isdir(SITE):
        for f in sorted(os.listdir(SITE)):
            p = os.path.join(SITE, f)
            if os.path.isfile(p):
                add(f, p)  # index.html / 各支页.html / robots.txt
        for sub in ("wallpapers", "thumbs"):
            d = os.path.join(SITE, sub)
            if os.path.isdir(d):
                for f in sorted(os.listdir(d)):
                    add(sub + "/" + f, os.path.join(d, f))
    return items

def upload_batch(user, passwd, batch):
    payload = []
    for rel, path in batch:
        data = open(path, "rb").read()
        payload.append(("file[]", (rel, data)))
    boundary = "----kisstr" + str(abs(hash(batch[0][0]))) + "----"
    body = b""
    for name, (filename, filedata) in payload:
        body += ("--" + boundary + "\r\n").encode()
        body += ('Content-Disposition: form-data; name="%s"; filename="%s"\r\n' % (name, filename)).encode("utf-8")
        body += b"Content-Type: application/octet-stream\r\n\r\n"
        body += filedata + b"\r\n"
    body += ("--" + boundary + "--\r\n").encode()
    req = urllib.request.Request("https://neocities.org/api/upload", data=body, method="POST")
    req.add_header("Content-Type", "multipart/form-data; boundary=" + boundary)
    token = base64.b64encode((user + ":" + passwd).encode("utf-8")).decode("ascii")
    req.add_header("Authorization", "Basic " + token)
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        return {"result": "error", "err": e.code, "msg": e.read().decode("utf-8", "replace")[:300]}

def delete_file(user, passwd, remote_path):
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
    print("共 %d 个文件待上传（site/ 平铺：index.html + 支页 + wallpapers/thumbs/robots）" % len(items))
    if not items:
        print("未找到 site/ 文件夹，请确认脚本与 site/ 同级")
        return
    user = input("Neocities 用户名: ").strip()
    passwd = getpass.getpass("Neocities 密码: ")

    # 清理旧结构残留（html/ 目录、assets/ 目录）
    build_legacy_clean()
    if LEGACY_CLEAN:
        print("清理旧结构 %d 个文件（html/ + assets/）..." % len(LEGACY_CLEAN))
        for i in range(0, len(LEGACY_CLEAN), BATCH):
            batch = LEGACY_CLEAN[i:i + BATCH]
            ok = fail = 0
            for rel in batch:
                r = delete_file(user, passwd, rel)
                if r.get("result") == "success":
                    ok += 1
                else:
                    fail += 1
            print("  清理 [%d/%d] 成功 %d 失败 %d" % (i + len(batch), len(LEGACY_CLEAN), ok, fail))

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
