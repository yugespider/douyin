import scrapy

from urllib.parse import urlencode
import execjs
from ..items import JdItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    # 请求api地址
    start_urls = ['https://search.jd.com/s_new.php']
    # 当前页
    page = 1
    # 累加值
    s = 1
    # 最大页
    max_page = 10
    # 逆向pvid
    node = execjs.get()
    # jd获取pvid的js代码 用execjs 解析 拿到结果赋值给请求参数的pvid
    js_code = """
    function pvid() {
        var a = (new Date).getTime();
        var b = "xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx".replace(/[xy]/g, function(b) {
            var c = (a + 16 * Math.random()) % 16 | 0;
            return a = Math.floor(a / 16),
            ("x" == b ? c : 3 & c | 8).toString(16)
        });
        return b
    }
    """
    ctx = node.compile(js_code, cwd='G:\spider\\node_modules')
    pvid = ctx.call('pvid')
    # 请求头 固定值
    headers = {
        "authority": "search.jd.com",
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://search.jd.com/Search?keyword=%E8%A1%A3%E6%9C%8D&wq=%E8%A1%A3%E6%9C%8D&pvid=aa352cacd3ce4644ba4b44e8c820ef8b&page=1&s=1&click=0",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    def parse(self, response):
        params = {
            "keyword": "黑丝",  # 查询的商品
            "pvid": self.pvid,  # 随机字符串 上边生成
            "page": self.page,  # 第一次 = 1
            "s": self.s,  # 第一次 = 1
            "click": "0",
        }
        # print('请求参数:', params) # 调试用 忽略
        # 回调给下边的方法提取数据
        yield scrapy.Request(self.start_urls[0] + '?' + urlencode(params), headers=self.headers, callback=self.get_data)

    # 提取数据
    def get_data(self, response):
        # 拿到返回的html大标签
        data = response.xpath('//div/ul')
        # 遍历父标签 从子标签里拿数据
        for d in data:
            # 定义items 在items.py 文件里定义字段,必须和下边的对应
            items = JdItem()
            # 获取商品 sku_id 列表, sku_id是商品唯一id 可以通过拼接网站+sku_id.html 访问详情页
            sku = d.xpath('./li/@data-sku').extract()
            # 获取商品价格 返回列表
            price = d.xpath('./li/div/div[@class="p-price"]//i/text()').extract()
            # 获取商品发货地 返回列表
            region = d.xpath('./li/div/div[@class="p-stock hide"]/@data-province').extract()
            # 获取商品店铺名 返回列表
            name = d.xpath('./li/div/div[@class="p-shop"]/span/a/text()').extract()
            # 获取商品详情页网址
            detail_url = d.xpath('./li/div/div[@class="p-commit"]/strong/a/@href').extract()
            # 拿到的都是列表 需要zip()
            sp = zip(sku, price, region, name, detail_url)
            # 得到zip对象sp 下边遍历sp对象取数据
            for s, p, r, n, detail in sp:
                items['sku'] = s
                items['price'] = p
                items['region'] = r
                items['name'] = n
                items['detail_url'] = 'https:' + detail
                yield items
        # 每次请求完 页码+1
        self.page += 1
        # 如果页码小于最大页 且 不是第二页 ，因为第二页需要self.s+=25
        if self.page < self.max_page and self.page != 2:
            self.s += 30
            # 回调self.parse 继续请求这个地址,但是请求参数变动了
            yield scrapy.Request(self.start_urls[0], dont_filter=True, callback=self.parse)
        elif self.page == 2:
            # 只有第二页是+=25
            self.s += 25
            yield scrapy.Request(self.start_urls[0], dont_filter=True, callback=self.parse)  # 请求相同URL需要设置 dont_filter=True
