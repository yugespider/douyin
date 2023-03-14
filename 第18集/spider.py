import requests
import execjs
import random
from urllib.parse import urlencode, unquote
import re
import time


class NewRank:
    def __init__(self, rank_name):
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.newrank.cn",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.rank_name = rank_name

    def get_xyz(self, h):
        node = execjs.get()
        with open('nonce_xyz.js', encoding='utf-8') as f:
            js_code = f.read()
        ctx = node.compile(js_code, cwd=r'D:\nodejs\node_modules\npm\node_modules')
        # 随机数
        xyz = ctx.call("run", h)
        return xyz

    def spider(self):
        url = "https://www.newrank.cn/xdnphb/main/v1/day/rank"  # 日榜
        # url = "https://www.newrank.cn/xdnphb/main/v1/week/rank"    # 周榜
        # url = "https://www.newrank.cn/xdnphb/main/v1/month/rank" # 月榜  rank_name_group:  全部 第一天-最后一天
        data = {
            "end": "2023-01-19",
            "rank_name": self.rank_name,
            "rank_name_group": "生活",
            "start": "2023-01-19",
            "nonce": '',
        }
        # python实现 js代码获取随机8位字符串
        c = ''
        b_list = [
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][random.randint(0, 15)] for
            i in range(8)]
        data['nonce'] = c.join(b_list)
        # 请求参数h拼接
        # '/xdnphb/main/v1/day/rank?AppKey=joker&end=2023-01-19&rank_name=文化&rank_name_group=生活&start=2023-01-19&nonce=c13cfad82'
        api = re.findall('https://www.newrank.cn(.*)', url)
        # 解码(拼接+固定值+编码)
        h = unquote(api[0] + '?AppKey=joker&' + urlencode(data))
        xyz = self.get_xyz(h)
        data['xyz'] = xyz
        response = requests.post(url, headers=self.headers, data=data).json()
        datas = response['value']['datas']
        for d in datas:
            print(d)


if __name__ == '__main__':
    type_list = ['文化', '百科', '健康', '时尚', '美食', '乐活', '旅行', '幽默', '情感', '体娱', '美体', '文摘', '民生', '财富', '科技', '创业', '汽车',
                 '楼市', '职场', '教育', '学术', '政务', '企业']
    for r in type_list:
        NewRank(r).spider()
        time.sleep(5)
