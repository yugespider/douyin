import ddddocr
import requests
import time
import execjs
import random
import re


# 网站地址 https://aq.99.com/V3/NDUser_Login.htm

class AL45:
    def __init__(self,username,password):
        self.headers = {
            "authority": "checkcode.99.com",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://aq.99.com/",
            "sec-ch-ua": "^\\^Not?A_Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^108^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        self.username = username
        self.password = password

    def get_code_url(self):
        time_str = round(float(time.time() * 1000))
        callback = "jQuery112403735179507214743_" + str(time_str)
        params = {
            "action": "getticket",
            "bussiness": "aq_login",
            "callback": callback,
            "_": time_str + 1
        }
        response = requests.get("https://checkcode.99.com/token", headers=self.headers, params=params)
        ticket = re.findall('ticket":"(.*)"', response.text)[0]
        params = {
            "CallBack": callback,
            "nduseraction": "getverifycodestate",
            "verifycodetype": "UserLogin",
            "bussiness": "aq_login",
            "ticket": ticket,
            "SiteFlag": "995",
            "RND": time.time(),
            "_": time_str + 2
        }
        response = requests.get("https://aq.99.com/AjaxAction/AC_verifycode.ashx", headers=self.headers, params=params)
        code_url = re.findall('https://.*[0-9]+', response.text)[0]
        return code_url


    def get_code(self):
        ocr = ddddocr.DdddOcr()
        res = requests.get(self.get_code_url(), headers=self.headers)
        open('1.jpg', 'wb').write(res.content)
        read_img = open('1.jpg', 'rb').read()
        code = ocr.classification(read_img)
        print('识别的验证码为：', code)
        return code


    def get_pwd(self,pwd):
        node = execjs.get()
        with open('1.js', encoding='utf-8') as f:
            js_code = f.read()
        ctx = node.compile(js_code, cwd=r'G:\spider\node_modules')
        password = ctx.call("run", pwd)
        return password


    def login(self):
        time_str = round(float(time.time() * 1000))
        callback = "jQuery112403735179507214743_" + str(time_str)
        pwd = self.get_pwd(self.password)
        code = self.get_code()
        params = {
            "CallBack": callback,
            "siteflag": "995",
            "nduseraction": "login",
            "txtUserName": self.username,
            "txtPassword": pwd,
            "checkcode": code,
            "Rnd": random.random(),
            "aws": "9356debff94debd66e77665d9532174f",
            "_": time_str
        }
        print("请求参数", params)
        response = requests.get("https://aq.99.com/AjaxAction/AC_userlogin.ashx", headers=self.headers, params=params)

        print(response.cookies)
        print(response.text)
        return response.text



if __name__ == '__main__':
    username = 你的账号
    password = 你的密码
    AL45(username=username,password=password).login()

