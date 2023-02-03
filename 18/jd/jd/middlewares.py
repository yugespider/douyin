# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random


class JdSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JdDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgentMiddleware():
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choices(self.user_agents)
        # 头部信息加这里


import time
from selenium import webdriver
# class JD:
#     # 初始化
#     def __init__(self, goods):
#         chrome_options = Options()
#         chrome_options.add_experimental_option('useAutomationExtension', False)
#         chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#         chrome_options.add_argument('--disable-blink-features=AutomationControlled')
#         self.browser = webdriver.Chrome(options=chrome_options)
#         self.goods = goods
#         self.headers = {
#             "authority": "img10.360buyimg.com",
#             "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#             "accept-language": "zh-CN,zh;q=0.9",
#             "cache-control": "max-age=0",
#             "if-modified-since": "Tue, 06 Dec 2022 07:40:01 GMT",
#             "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "\"Windows\"",
#             "sec-fetch-dest": "document",
#             "sec-fetch-mode": "navigate",
#             "sec-fetch-site": "none",
#             "sec-fetch-user": "?1",
#             "upgrade-insecure-requests": "1",
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#         }
#
#     # 主页搜索
#     def base(self):
#         self.browser.get('https://www.jd.com/')
#         search = self.browser.find_element(By.XPATH, '//*[@id="key"]')
#         search.send_keys(self.goods)
#         self.browser.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click()
#
#     def drop_down(self):
#         for x in range(1, 10):
#             j = x / 10
#             js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}"
#             self.browser.execute_script(js)
#             time.sleep(random.randint(400, 800) / 1000)
#
#     # 抓取数据
#     def spider(self):
#         self.drop_down()
#         div = self.browser.find_elements(By.CLASS_NAME, 'gl-i-wrap')
#         for d in div:
#             shop_name = d.find_element(By.XPATH, './/span/a')
#             title = d.find_element(By.XPATH, './/div[@class="p-name p-name-type-2"]/a')
#             price = d.find_element(By.XPATH, './/div[@class="p-price"]//i')
#             # tag = d.find_element(By.XPATH,'.//div[@class="p-icons"]/i')
#             url = d.find_element(By.XPATH, './/div[@class="p-name p-name-type-2"]/a').get_attribute('href')
#             # img_url = d.find_element(By.XPATH, './/div[@class="p-img"]/a/img').get_attribute('src')
#             # print(img_url)
#             sku_id = re.search('^http.*/(\d+)', url).group(1)
#             data = {
#                 '店铺': shop_name.text,
#                 '标题': title.text,
#                 '价格': price.text,
#                 # '标签': [t.text for t in tag],
#                 'url': url,
#                 'sku_id': sku_id,
#                 # 'img_url': img_url
#             }
#             # if img_url:
#             #     response = requests.get(img_url, headers=self.headers)
#             #     print(response.content)
#             #     with open(f"{title.text}.jpg", 'wb') as f:
#             #         f.write(response.content)
#             #         f.close()
#             # self.save_mongo(items)
#             print(data)
#         self.page_next()
#
#     # 入库
#     # 翻页
#     def page_next(self):
#         try:
#             next = self.browser.find_element(By.XPATH, "//div[@class='page clearfix']/div/span/a[@class='pn-next']")
#             if next:
#                 next.click()
#                 self.spider()
#             else:
#                 self.browser.close()
#         except Exception as e:
#             print(e)
#
#     def run(self):
#         self.base()
#         self.spider()
