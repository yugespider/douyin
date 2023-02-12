from flask import Flask,request,jsonify
import requests
import ddddocr
app = Flask(__name__)


def get_img_code(url):
    ocr = ddddocr.DdddOcr()
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://xkczb.jtw.beijing.gov.cn/",
        "Sec-Fetch-Dest": "image",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "sec-ch-ua": "^\\^Not?A_Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^108^^, ^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    res = requests.get(url,headers=headers)
    open('1.jpg','wb').write(res.content)
    read_img = open('1.jpg','rb').read()
    code = ocr.classification(read_img)
    return code


@app.route('/index',methods=['GET'])
def index():
    key = request.args.get('key')
    if key != '123123':
        return jsonify({'status':False,'code':None})

    url = request.args.get('img')
    code = get_img_code(url)
    return jsonify({'status':True,'code':code})

if __name__ == '__main__':
    app.run(port=50001)
