import requests
import json
import execjs



def get_sign(param):
    node = execjs.get()
    with open('sign.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code, cwd=r'D:\nodejs\node_modules\npm\node_modules')
    sign = ctx.call("getSign", param)
    return sign


def spider(eng):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Acs-Token": "1672214772966_1672285245724_46YD4T20bk2GGOtvQ50qSpBjz8WsKwVrhsVmLkFBXTaUqgZC5WL/Dx7XrKXV1M+/MSTI+jRxJYwxvg9bYoswESpQuZQwOgxi6Jqpu5+e2ptq4tAUl/VgoWYssEdF1tJ1Z+Mq2W7xl2vm5lJCrbuy2GgjvyFoVOAwVWbkxIg1ZmqluRcOXgDSsfQAtCy1yi8rcctGaV1HWAPrtUV79vhMlEmkAS3U7GzSk/4fsIct6F66cu1hat2G/HMgf7rbeyF3xXi/Z8TZ3lJ7qIbVZBpgPTzLo5uT3VzE6uH7+HZX5Q63/TnsE4wYgsPnbVP88O6m",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://fanyi.baidu.com",
        "Referer": "https://fanyi.baidu.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "BIDUPSID": "CB6B226CB80A125DF76BAA90201C809C",
        "PSTM": "1670909343",
        "APPGUIDE_10_0_2": "1",
        "REALTIME_TRANS_SWITCH": "1",
        "FANYI_WORD_SWITCH": "1",
        "HISTORY_SWITCH": "1",
        "SOUND_SPD_SWITCH": "1",
        "SOUND_PREFER_SWITCH": "1",
        "ZFY": "m5Zbw5icbpSA3nQuPfEwoXb2Hd:BtHlluaPYxL9EY7Mg:C",
        "BDORZ": "FFFB88E999055A3F8A630C64834BD6D0",
        "BAIDU_WISE_UID": "wapp_1672193944875_551",
        "__bid_n": "1855688092a9e8ec6f4207",
        "FEID": "v10-7fdd2a3031c1ac07cf7feb4b019efe4fe23a0385",
        "__xaf_fpstarttimer__": "1672194034064",
        "__xaf_thstime__": "1672194034145",
        "FPTOKEN": "+DkJBYeysPglc/F37OPLHorZyGFL4pBIMS4Fsd430Rb9gcafonSxrD0GJjcUgePn0s7ySQuX8loyMTXLDnRQDIogPk8KrBYg+WIXywrLfbxRIDUkUTFfLTqW9SfWvplDaENfGBRNzyS4DN6EZUTlgPFTX/M6tMgwr/RyCdjVbhrSdHXchfkhfWR++MABSH4C905eztnwR5LLW9EhySwCvMqwPzY4zJOCFfn40Hz6v9PNSN+n9YSZXNEgME1hKFBFd+0ZgIm6PkaTtoiZW2m70Wj3H/DZmL+KA25Wqe+2MHVNSq/aT4dwom7drfDFFiPV691bHcaCdrdq1bnJuGhmj/AgXdHYp67YHa/6TVA6YTBwZHpyB85+Ug9kKZnaKZVSKhNXUDEgHBpFvd/L+J+Yng==|oZqhY7iyiFMA+VjPjlaYfWT6n15ShuIpSvTJ7xxspoQ=|10|dc6ddf9ead8928c69d9f77e81c5a6a57",
        "__xaf_fptokentimer__": "1672194034261",
        "BAIDUID": "8B308BBEA99FE6741FBEE7FB9ECD91D4:SL=0:NR=10:FG=1",
        "BAIDUID_BFESS": "8B308BBEA99FE6741FBEE7FB9ECD91D4:SL=0:NR=10:FG=1",
        "BDRCVFR[yxi3RW9Ex4T]": "L9mSQZcCfu6Tg7CpAC8mvqV",
        "delPer": "0",
        "PSINO": "2",
        "H_PS_PSSID": "26350",
        "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574": "1670990593,1670999545,1672278710",
        "BDUSS": "3dqRlYtWktvV0JLUWtGMW9ybHl1TXNYZ0V0dHNHWWZVbjRyLWNGaUIxUXJrdFJqRVFBQUFBJCQAAAAAAAAAAAEAAAABt18MRGVhdGhGaXNoV1NZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACsFrWMrBa1ja",
        "BDUSS_BFESS": "3dqRlYtWktvV0JLUWtGMW9ybHl1TXNYZ0V0dHNHWWZVbjRyLWNGaUIxUXJrdFJqRVFBQUFBJCQAAAAAAAAAAAEAAAABt18MRGVhdGhGaXNoV1NZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACsFrWMrBa1ja",
        "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574": "1672284956",
        "ab_sr": "1.0.1_ZTliZjNmMjVlYzU4ZWQxZTZkYjFhOTljOTNhY2UwYzVjZGM1Y2M0MzgxZmNlYTczMGRkYWFjZTU5OGEwZWRkMzZkN2IyZTRjNTU5ZjE4NmEwZDMwMWNkMzQxMzVmZDkxZTY0YmU2YzkxMDYzZDlmYmFiN2M5YTA4MGEzYjRkMGEwMGE1NjEyYmExMDZjOWZjNzk1MDA5ZmRkOGM2ODNkMmJiMWMyNzdjNGFiMGZlMmMxYzIzZWRmM2Y4MWYzMjM5"
    }
    url = "https://fanyi.baidu.com/v2transapi"
    params = {
        "from": "en",
        "to": "zh"
    }
    sign = get_sign(eng)
    data = {
        "from": "en",
        "to": "zh",
        "query": eng,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": sign,
        "token": "a385233a2163cff372dd2380c1b182f8",
        "domain": "common"
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    a = json.loads(response.text)
    res = a['trans_result']['data'][0]['dst']
    print("翻译结果:", res)


if __name__ == '__main__':
    while True:
        eng = input('输入英文:')
        spider(eng)
        q = input('是否继续?y/n')
        if q == 'y':
            continue
        elif q == 'n':
            break
        else:
            print('请输入y/n')
