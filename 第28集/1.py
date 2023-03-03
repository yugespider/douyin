import requests
from Crypto.Cipher import AES
import re

class DecodeM3u8:
    def __init__(self, m3u8_url=None):
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Origin": "https://www.ocplayer.com",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "sec-ch-ua": "^\\^Not?A_Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^108^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }
        self.m3u8_url = m3u8_url

        self.ts_list = []
        self.key = b''
        self.iv = b'0000000000000000'
        self.aes_obj = None

    def getKey(self):
        # 请求M3U8拿到KEY
        m3u8 = requests.get(self.m3u8_url, headers=self.headers).text
        key_url = re.findall('#EXT-X-KEY.*URI="(.*)"',m3u8)
        key = bytes(requests.get(key_url[0], headers=self.headers).text,encoding='utf-8')
        self.ts_list = re.findall('https://.*.ts',m3u8)
        self.aes_obj = AES.new(key, AES.MODE_CBC, self.iv)

    def ts(self):
        res = requests.get(self.ts_list[0], headers=self.headers).content

        # 解密
        with open('jiemi.mp4','ab') as f:
            f.write(self.aes_obj.decrypt(res))


    def run(self):
        self.getKey()
        self.ts()



if __name__ == '__main__':
    DecodeM3u8(m3u8_url="你的M3U8").run()
