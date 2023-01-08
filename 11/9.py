import requests
from lxml import etree
import json
import time


def get_token():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Referer": "http://www.customs.gov.cn/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    url = "http://gss.customs.gov.cn/clsouter2020/Home/ClassifyYCDSearch"
    res = requests.get(url, headers=headers, verify=False)
    input = etree.HTML(res.text)
    token = input.xpath("//body/input[@name='__RequestVerificationToken']/@value")[0]
    cookie = res.cookies.get('__RequestVerificationToken_L0NMU291dGVyMjAyMA2')
    return token, cookie


def spider(token, cookie):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://gss.customs.gov.cn",
        "Referer": "http://gss.customs.gov.cn/clsouter2020/Home/ClassifyYCDSearch",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    cookies = {
        "__jsluid_h": "1267a0e1796fa20ebc9ae0fe64e98e5e",
        "__RequestVerificationToken_L0NMU291dGVyMjAyMA2": cookie
    }
    url = "http://gss.customs.gov.cn/CLSouter2020/Search/GetQuerySearchList"
    data = {
        "__RequestVerificationToken": token,
        "page": "3",
        "pageSize": "20",
        "Type": "YCD",
        "SourceNo": "",
        "GName": "",
        "CodeTS": "",
        "GMdel": "",
        "EngName": "",
        "OtherName": ""
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False).text
    data = json.loads(response)['data']
    # 相关编号：SOURCE_NO
    # 中文名称：G_NAME
    # 决定税号：CODE_TS
    # 规格型号: G_MODEL
    for d in data:
        data_dict = {}
        data_dict['相关编号'] = d['SOURCE_NO']
        data_dict['中文名称'] = d['G_NAME']
        data_dict['决定税号'] = d['CODE_TS']
        data_dict['规格型号'] = d['G_MODEL']
        print(data_dict)


if __name__ == '__main__':
    page = 5
    for i in range(1, page + 1):
        print(f'正在抓取第{i}页:')
        token, cookie = get_token()
        time.sleep(1)
        spider(token, cookie)
