import requests
import ddddocr
import time
import execjs
# https://www.fcbox.com/pages/user/login.html

class FengChaoLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()
        self.headers = {
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://www.fcbox.com/pages/user/login.html",
            "Sec-Fetch-Dest": "image",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }

    def get_code(self):
        url = "https://www.fcbox.com/captcha/getVerifyCodeImg"
        response = requests.get(url, headers=self.headers)
        open('code.jpg', 'wb').write(response.content)
        self.session.cookies = response.cookies
        ocr = ddddocr.DdddOcr()
        img_bytes = open('code.jpg', 'rb').read()
        code = ocr.classification(img_bytes)
        return code

    def encrypt_password(self):
        node = execjs.get()
        js_code = open('1.js', 'r', encoding='utf-8').read()
        ctx = node.compile(js_code, cwd=r'D:\spider\node_modules')
        pwd = ctx.call("encrypt", self.password)

        return pwd

    def login(self):
        url = "https://www.fcbox.com/passport/login"
        params = {
            "username": self.username,
            "password": self.encrypt_password(),
            "verifyCode": self.get_code(),
            "_": round(float(time.time() * 1000))
        }
        response = self.session.get(url, headers=self.headers, params=params)
        print(response.text)
        print(response.cookies)


if __name__ == '__main__':
    FengChaoLogin(username='17610103375', password='Wsy19921030').login()
