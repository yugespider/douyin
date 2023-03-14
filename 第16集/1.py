import requests
import execjs
import datetime


class QiMai:
    def __init__(self,brand,device):
        self.headers = {
            "authority": "api.qimai.cn",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "origin": "https://www.qimai.cn",
            "referer": "https://www.qimai.cn/",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        self.brand = brand
        self.device = device

    def get_analysis(self):
        node = execjs.get()
        with open('kou.js', encoding='utf-8') as f:
            js_code = f.read()
        ctx = node.compile(js_code, cwd='G:\spider\\node_modules')
        e = ctx.call('run',self.brand,self.device)
        return e

    def spider(self):
        analysis = self.get_analysis()
        print(analysis)
        url = "https://api.qimai.cn/rank/index"
        params = {
            "analysis": analysis,
            "brand": self.brand,
            "device": self.device,
            "country": "cn",
            "genre": "36",
            # 翻页需要的参数
            # "date": str(datetime.date.today()),
            # "page": "1"
        }
        response = requests.get(url, headers=self.headers, params=params).json()
        data = response['rankInfo']
        for d in data:
            print(d)

    def run(self):
        self.spider()



if __name__ == '__main__':
    # brand: grossing 畅销
    # paid 收费
    # free 免费
    b = 'paid'
    # device: ipad /iphone
    d = 'iphone'
    QiMai(brand=b, device=d).run()
