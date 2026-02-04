import requests
from urllib.parse import urljoin

BASE_URL = "https://ua-dev.tesoon.com"
CAPTCHA_REFRESH_API = "/admin/index/captcha?refresh=1"

# 浏览器 UA，防止被简单拦
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/144.0.0.0 Safari/537.36"
    ),
    "X-Requested-With": "XMLHttpRequest",
}

def fetch_captcha(save_path="captcha.png"):
    session = requests.Session()
    session.headers.update(HEADERS)

    # 1️⃣ 刷新验证码（生成 session 中的验证码）
    refresh_url = urljoin(BASE_URL, CAPTCHA_REFRESH_API)
    resp = session.get(refresh_url, timeout=10)
    resp.raise_for_status()

    data = resp.json()
    captcha_url = data.get("url")
    if not captcha_url:
        raise RuntimeError(f"未获取到 captcha url，返回内容：{data}")

    # 2️⃣ 请求验证码图片（必须同一 session）
    image_url = urljoin(BASE_URL, captcha_url)
    img_resp = session.get(image_url, timeout=10)
    img_resp.raise_for_status()

    # 3️⃣ 保存图片
    with open(save_path, "wb") as f:
        f.write(img_resp.content)

    print(f"✅ 验证码已保存：{save_path}")
    return save_path


if __name__ == "__main__":
    fetch_captcha()
