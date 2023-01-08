import requests
import json
from datetime import datetime


class Wb:
    def __init__(self, filename):
        self.headers = {
            "authority": "weibo.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "client-version": "v2.37.11",
            "referer": "https://weibo.com/1878335471/LtocQsOjx",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "server-version": "v2022.12.15.1",
            "traceparent": "00-162afabfd10619d3af77bba202ed030e-d0e7866930df6ac3-00",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": "W841k0GlhrCDw7zbxFU0JPRm"
        }
        self.cookies = {
            "SINAGLOBAL": "5448314086224.435.1671021524800",
            "ULV": "1671021524870:1:1:1:5448314086224.435.1671021524800:",
            "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9Whrwo-TCqOCox4nLr-gHuyd5JpX5KMhUgL.Fo-0SKepeo-4S0-2dJLoI7UN9PULdspX",
            "WBPSESS": "g4PRVr4rcEOGWf-jmqeylpls2dN8El7vq8oa2jEmXgEvPdETQ0HOBiX07xJF2e7_zKHMd6aVYRs2WG3KbSDwlVdP0TEwCFcVlrC56NNFxfTaRZ8E5lHG_B6B5DQhg004_885UGPqP6apeUxDND3ikw==",
            "PC_TOKEN": "fb4171790f",
            "ALF": "1673728859",
            "SSOLoginState": "1671136859",
            "SCF": "AuKbT07OCoK-dV7Y_AUbNgSr3wH39LHoaprVF3xcr2MnpoZ0DXZihMyo1xALc9QSNbnbdOEJS_WgUdDbQWNYwnU.",
            "SUB": "_2A25On_YLDeRhGeNN7lEQ8ivFzDmIHXVt7WDDrDV8PUNbmtAKLXjskW9NSVXhjFvc8it_FvVtbxIVbKeBrGYxTa3d",
            "XSRF-TOKEN": "W841k0GlhrCDw7zbxFU0JPRm"
        }
        self.max_id = 0
        self.page = 0
        self.max_page = 5
        self.file = filename

    def spider(self):
        url = "https://weibo.com/ajax/statuses/buildComments"
        params = {
            "is_reload": "1",
            # 文章ID 爬其他需要改这个
            "id": "4770045646866595",
            "is_show_bulletin": "2",
            "is_mix": "0",
            "count": "20",
            "max_id": self.max_id,
            # user id 看情况修改
            "uid": "1878335471"
        }
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)
        res_dict = json.loads(response.text)
        # print(res_dict)
        for i in res_dict['data']:
            items = {}
            items['用户ID'] = i['user']['id']
            items['用户名'] = i['user']['screen_name']
            fbtime = datetime.strptime(i["created_at"], '%a %b %d %H:%M:%S +0800 %Y')
            items['发布时间'] = str(fbtime)
            items['评论内容'] = (i['text'])
            with open(self.file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(items, indent=2, ensure_ascii=False))
                f.write(',')
            # print(items)
        # print(res_dict['max_id'])
        self.max_id = res_dict['max_id']
        self.page += 1
        if self.page <= self.max_page:
            self.spider()


if __name__ == '__main__':
    file = 'data1.json'
    wb = Wb(file)
    wb.spider()
    # open(file, 'a', encoding='utf-8').write('[\n')

    # with open(file, 'rb+') as f:
    #     f.seek(-1, os.SEEK_END)
    #     f.truncate()
    # open(file, 'a', encoding='utf-8').write('\n]')
