import requests
import execjs
import json

def get_sign():
    node = execjs.get()
    with open('sign.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code, cwd='G:\spider\\node_modules')
    sign = ctx.call('run')
    return sign[0], sign[1]


def decode_data(data):
    node1 = execjs.get()
    with open('decode.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node1.compile(js_code, cwd='G:\spider\\node_modules')
    text = ctx.call('run', data)
    return text


def spider(k):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://fanyi.youdao.com",
        "Referer": "https://fanyi.youdao.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "OUTFOX_SEARCH_USER_ID": "-923326740@10.105.137.204",
        "OUTFOX_SEARCH_USER_ID_NCOO": "1824996015.7015798",
        "NTES_YD_PASSPORT": "AjQiiee0aE.hyM58dnw9MCMe3.7J5X9_lR956EhBzuMzFjMNF3qU1PYArb58czK2yoMLXG0lPLPh7odLf1EvkkMBCWA5Jw16OMVlgp54jvLgwuxStcWZcXr3WZHqRw6NbEO4jVhUh0qTwpyS.t7w8pS2IvMEmDlBrR_r7aMsFFsAniMxNZXGzqMzu0P0DWQAlS2Sj7LRQrNX0WybclCkKnl.NXc0ZmRO2",
        "P_INFO": "17600259756|1672643708|1|dict_logon|00&99|null&null&null#bej&null#10#0|&0||17600259756",
        "YOUDAO_MOBILE_ACCESS_TYPE": "0"
    }
    url = "https://dict.youdao.com/webtranslate"
    sign, mysticTime = get_sign()
    data = {
        "i": str(k),
        "from": "auto",
        "to": "",
        "domain": "0",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": sign,
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": mysticTime,
        "keyfrom": "baidufanyi.web"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    return response.text


if __name__ == '__main__':
    while True:
        eng = input('输入英文,别的别瞎JB输入：')
        encode_txt = spider(eng)
        # print(encode_txt)
        res = json.loads(decode_data(encode_txt))['dictResult']['ec']['word']['trs']
        for i in res:
            print(i)