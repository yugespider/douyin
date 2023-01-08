import requests
import re
import os
import time
import urllib3


class DownloadMovie:
    def __init__(self, m_url, m_directory):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; DUK-AL20 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.120 Mobile Safari/537.36",
            "allow-cross-domain-redirect": "false",
            "Host": "v8.dious.cc"
        }
        # 这两步 不加会报错
        self.session = requests.Session()
        self.session.trust_env = False
        # url和文件名从外边传进来
        self.m_url = m_url
        self.m_directory = m_directory

    def mk_movie_dir(self):
        d = os.path.exists(self.m_directory)
        if not d:
            os.mkdir(self.m_directory)
            return True

    def download_m3u8(self):
        response = self.session.get(self.m_url + '/index.m3u8', headers=self.headers, verify=False)
        with open(f'./{self.m_directory}/index.m3u8', 'w', encoding='utf-8') as f:
            f.write(response.text)

    def download_movie(self):
        with open(f'./{self.m_directory}/index.m3u8', 'r', encoding='utf-8') as f:
            file = f.read()
            # 如果是其他结尾就改一下括号里的
            ts_list = re.findall('(.*.ts)', file)

        for ts in ts_list:
            response = self.session.get('https://v8.dious.cc/' + ts, headers=self.headers)
            print("下载地址为：", 'https://v8.dious.cc' + ts)
            with open(f'{self.m_directory}/{self.m_directory}.avi', 'ab+') as f:
                f.write(response.content)
                print("下载完成->", ts)
                time.sleep(1)

    def run(self):
        # 关闭警告信息
        urllib3.disable_warnings()
        mkdir = self.mk_movie_dir()
        if mkdir:
            self.download_m3u8()
            self.download_movie()


if __name__ == '__main__':
    # 定义名称 文件夹和电影文件名称
    movie_name = '麦道夫'
    # 抓包拿到的接口地址 结尾是hls 没有/
    movie_url = "https://v8.dious.cc/20230104/jSrHQAEG/1500kb/hls"
    DownloadMovie(m_url=movie_url, m_directory=movie_name).run()
