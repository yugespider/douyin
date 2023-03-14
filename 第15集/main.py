# 网站地址 http://www.hh1024.com/
# 这个网站是单点登录 一个账号同一时间只有一个token有效
import hashlib
import time
import requests
import json


class HongRen:
    def __init__(self, username, password, txt):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "http://www.hh1024.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        # 用session方式请求
        self.session = requests.session()
        self.session.headers = self.headers
        # 你的账号密码 从外边传进来
        self.username = username
        self.password = password
        # 时间戳处理
        self.times = round(time.time() * 1000)
        # 搜索的分类
        self.txt = txt
        # token
        self.token = ''

    # 登录请求参数pwd和sig
    def get_sig(self):
        k = 'JzyqgcoojMiQNuQoTlbR5EBT8TsqzJ'
        password = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        n = self.username + password + str(self.times) + '1' + k
        # md5(用户名+密码md5+tenant值+时间戳+固定值)
        sig = hashlib.md5(n.encode('utf-8')).hexdigest()
        return [password, sig]

    # 模拟登录请求
    def login(self):
        url = "https://user.hrdjyun.com/wechat/phonePwdLogin"
        # 获取两个请求参数
        password, sig = self.get_sig()
        data = {
            "phoneNum": self.username,
            "pwd": password,
            "t": self.times,
            "tenant": 1,
            "sig": sig
        }
        data = json.dumps(data)
        response = self.session.post(url, data=data).json()
        # 获取响应的token
        tk = response['data']['token']
        # 赋值给self.token
        self.token = tk

    def spider(self, tk):
        data = {
            "param": "{\"no\":\"dy0000\",\"data\":{\"user_label\":\"%s\"}}" % self.txt,
            "sign": "",
            "tenant": "1",
            "timestamp": self.times + 3,
            "token": tk
        }
        # 拼接参数然后sha256算法 得到sign
        par = "param=" + data['param'] + "&timestamp=" + str(
            self.times + 3) + "&tenant=1&salt=" + 'kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$'
        sign = hashlib.sha256(par.encode('utf-8')).hexdigest()
        data['sign'] = sign
        url = "https://ucp.hrdjyun.com:60359/api/dy"
        response = self.session.post(url, headers=self.headers, data=json.dumps(data)).json()
        # 已经可以返回值了 后续数据自己处理吧 想要什么拿什么
        print(response['data'])

    def run(self):
        # 登录
        self.login()
        if self.token:
            print(f'登录成功,获取的token为:{self.token}')
        # 登录成功后休息3秒
        print('缓缓劲儿 歇三秒')
        time.sleep(3)
        # 爬取 需要带token
        print('开爬')
        self.spider(self.token)
        print('爬完了')


if __name__ == '__main__':
    user = '你的账号'
    pwd = '你的密码'
    # 分类 你要搜的东西
    text = '网红帅哥'  # 网红美女 网红帅哥 搞笑 情感 剧情 美食 美妆 种草 穿搭 明星 影视娱乐 游戏宠物 音乐 舞蹈 萌娃 生活 健康 体育 旅行 动漫 创意 时尚 母婴育儿 教育 职场教育 汽车 家居 科技
    # 太多了另起一行
    # 摄影教学 政务 知识资讯类 办公软件
    HongRen(user, pwd, text).run()
