import requests
from lxml import etree
import execjs
import re
# http://ggzy.zwfwb.tj.gov.cn/
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://ggzy.zwfwb.tj.gov.cn/jyxxzfcg/index_2.jhtml",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "http://ggzy.zwfwb.tj.gov.cn/jyxxzfcg/index_1.jhtml"
response = requests.get(url, headers=headers, verify=False)

html = etree.HTML(response.text)
# url_list = html.xpath('//div[@class="article-content"]/ul/li/div/a/@url')
# print(url_list)
url_list= ['http://ggzy.zwfwb.tj.gov.cn:80/jyxxcggg/1006981.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcggg/1006980.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcggg/1006979.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcggg/1006990.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxzcgz/1006978.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcgjg/1006985.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcgjg/1006983.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcgjg/1006991.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcgjg/1006989.jhtml', 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcgjg/1006982.jhtml']

def encrypt_url(aa,ccc):
    node = execjs.get()
    with open('1.js',encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code,cwd=r'G:\spider\node_modules')
    url = ctx.call('encrypt',ccc,aa)
    return url

for url in url_list:
    aa = url.split('/')
    ccc = re.findall('http://.*?([0-9]+).jhtml',url)
    print(encrypt_url(aa,ccc))