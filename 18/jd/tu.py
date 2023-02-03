import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType  # 主题类型

# 读取json文件
df = pd.read_json('data.json', encoding='utf-8')
# 拿到价格列表
price_list = [int(i) for i in df['price']]
# 拿到店铺列表
dp_list = [d for d in df['name']]

# 商品价格和店铺名柱状图
b = Bar(init_opts=opts.InitOpts(chart_id='1', theme=ThemeType.LIGHT))
b.add_xaxis(dp_list)
b.add_yaxis("商品价格", price_list)
b.set_global_opts(title_opts=opts.TitleOpts(title="价格", pos_left='30px'))

# 圆圈百分比图1
allP = len(price_list)
liquid = Liquid(init_opts=opts.InitOpts(chart_id='2', theme=ThemeType.LIGHT))
liquid.set_global_opts(title_opts=opts.TitleOpts(title="价格500以上占比", pos_left='30px'))
p500 = len([p for p in price_list if p > 500])
liquid.add('500块钱以上占比', [p500 / allP])
# 圆圈百分比图2
liquid2 = Liquid(init_opts=opts.InitOpts(chart_id='3', theme=ThemeType.LIGHT))
liquid2.set_global_opts(title_opts=opts.TitleOpts(title="价格1000以上占比", pos_left='30px'))
p1000 = len([p for p in price_list if p > 1000])
liquid2.add('1000块钱以上占比', [p1000 / allP])
# 圆圈百分比图3
liquid3 = Liquid(init_opts=opts.InitOpts(chart_id='4', theme=ThemeType.LIGHT))
liquid3.set_global_opts(title_opts=opts.TitleOpts(title="价格100以下占比", pos_left='30px'))
p100 = len([p for p in price_list if p < 100])
liquid3.add('100块钱以下占比', [p100 / allP])
# 圆圈百分比图4
p2000 = len([p for p in price_list if p > 2000])
liquid4 = Liquid(init_opts=opts.InitOpts(chart_id='5', theme=ThemeType.LIGHT))
liquid4.set_global_opts(title_opts=opts.TitleOpts(title="价格2000以上占比", pos_left='30px'))
liquid4.add('2000块钱以上占比', [p2000 / allP])

# 同一价格出现次数柱状图
count_dist = {}
for i in price_list:
    if i in count_dist:
        count_dist[i] += 1
    else:
        count_dist[i] = 1

b2 = Bar(init_opts=opts.InitOpts(chart_id='6', theme=ThemeType.LIGHT))
b2.add_xaxis(list(count_dist.keys()))
b2.add_yaxis("同一价格出现的次数", list(count_dist.values()))
b2.set_global_opts(title_opts=opts.TitleOpts(title="同一价格出现的次数", pos_left='30px'))

# 1000元以上价格慈云
price_cloud1 = [(k, v) for k, v in count_dist.items() if k > 1000]
c1 = WordCloud(init_opts=opts.InitOpts(chart_id='7', theme=ThemeType.LIGHT))
c1.add("", price_cloud1, word_size_range=[20, 100], shape='cardioid')
c1.set_global_opts(title_opts=opts.TitleOpts(title="1000元以上商品价格词云", pos_left='30px'))

# 100元以下价格图
price_cloud2 = [(k, v) for k, v in count_dist.items() if k < 100]
c2 = WordCloud(init_opts=opts.InitOpts(chart_id='8', theme=ThemeType.LIGHT))
c2.add("", price_cloud2, word_size_range=[20, 100], shape='cardioid')
c2.set_global_opts(title_opts=opts.TitleOpts(title="100元以下商品价格词云", pos_left='30px'))

# 100-500元商品价格词云图
price_cloud3 = [(k, v) for k, v in count_dist.items() if k > 100 and k < 500]
c3 = WordCloud(init_opts=opts.InitOpts(chart_id='9', theme=ThemeType.LIGHT))
c3.add("", price_cloud3, word_size_range=[20, 100], shape='cardioid', pos_left='30px')
c3.set_global_opts(title_opts=opts.TitleOpts(title="100-500元商品价格词云"))

# 500-1000元商品价格词云图
price_cloud4 = [(k, v) for k, v in count_dist.items() if k > 500 and k < 1000]
c4 = WordCloud(init_opts=opts.InitOpts(chart_id='10', theme=ThemeType.LIGHT))
c4.add("", price_cloud4, word_size_range=[20, 100], shape='cardioid')
c4.set_global_opts(title_opts=opts.TitleOpts(title="500-1000元商品价格词云", pos_left='30px'))

# 两个列表合并成字典
dp_price_dict = dict(zip(price_list, dp_list))

# 列表排序
price_list = sorted(price_list)

# 最贵top10
ex_top10 = price_list[-10:][::-1]
top10dp = [[dp_price_dict[i], i] for i in ex_top10]
f = Funnel(init_opts=opts.InitOpts(chart_id='11', theme=ThemeType.LIGHT))
f.add('最贵top10店家', top10dp)
f.set_global_opts(title_opts=opts.TitleOpts(title="最贵top10店家名称", pos_top='300px'))

# 最便宜top10
py_top10 = price_list[:10]
py_top10dp = [[dp_price_dict[i], i] for i in py_top10]
f1 = Funnel(init_opts=opts.InitOpts(chart_id='12', theme=ThemeType.LIGHT))
f1.add('最便宜top10店家', py_top10dp)
f1.set_global_opts(title_opts=opts.TitleOpts(title="最便宜top10店家名称", pos_top='300px'))

# 不可拖拽缩放的标签页列类型
tab = Tab()
# tab.add(b, "柱状图")
# tab.add(liquid, "水球图")
# print(price_list.sort())
# print(price_list)
# tab.render("1.html")


page = Page(layout=Page.DraggablePageLayout)
# 输出几张图
page.add(b, liquid, liquid2, liquid3, liquid4, b2, c1, c2, c3, c4, f, f1)
# 生成一个html文件
page.render("index.html")
page.save_resize_html("index.html", cfg_file="chart_config.json", dest="排版之后的图.html")
