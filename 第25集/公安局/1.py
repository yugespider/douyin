import requests
import re
import execjs


def get_cookies():
    headers = {
        "Host": "www.mps.gov.cn",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.mps.gov.cn/n2253534/n4904351/index.html",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    url = "https://www.mps.gov.cn/n2253534/n4904351/index.html"
    response = requests.get(url, headers=headers)
    __jsluid_s = response.cookies.get('__jsluid_s')
    dom_cookie = re.findall(r".*cookie=(.*?);location.*", response.text)[0]
    __jsl_clearance_s = execjs.eval(dom_cookie).split(";")[0]
    return __jsluid_s, __jsl_clearance_s


# 第二张
def get_go_params(c1, c2):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.mps.gov.cn/n2253534/n4904351/index.html",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "__jsluid_s": c1,
        "__jsl_clearance_s": c2[18:]
    }
    url = "https://www.mps.gov.cn/n2253534/n4904351/index.html"
    res = requests.get(url, headers=headers, cookies=cookies)
    go_params = re.findall(r';go\((.*)\)</script>', res.text)[0]
    return go_params


def get_index_page(c1, params):
    node = execjs.get()
    with open('1.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code, cwd=r'G:\spider\node_modules')
    __jsl_clearance_s = ctx.call("run", params)
    headers = {
        "Accept": "text/html, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.mps.gov.cn/n2253534/n4904351/index.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "^\\^Not?A_Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^108^^, ^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    cookies = {
        "maxPageNum7574611": "786",
        "__jsluid_s": c1,
        "__jsl_clearance_s": __jsl_clearance_s
    }
    url = "https://www.mps.gov.cn/n2253534/n4904351/c8862492/content.html"
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.text)


if __name__ == '__main__':
    __jsluid_s, __jsl_clearance_s = get_cookies()
    go_params = get_go_params(__jsluid_s, __jsl_clearance_s)
    get_index_page(__jsluid_s, go_params)
