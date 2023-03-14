from scrapy import cmdline

# cmdline.execute('scrapy crawl doubanmoive_spider -o res.json'.split())
with open('data.json','w') as f:
    f.truncate()
    f.close()

cmdline.execute('scrapy crawl jd -o data.json -s FEED_EXPORT_ENCODING=utf-8'.split())