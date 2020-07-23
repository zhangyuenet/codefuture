#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from pyecharts import options as opts
from pyecharts.charts import Map,MapGlobe
import pyecharts.options as options


url = 'https://www.worldometers.info/world-population/population-by-country/'


header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
r = requests.get(url, headers=header)
htmldata = etree.HTML(r.text)

data = []

countries = htmldata.xpath('//table[@id="example2"]/tbody/tr')
for country in countries:
    name = country.xpath('td[2]/a/text()')[0]
    population = country.xpath('td[3]/text()')[0]
    population = int(population.replace(',',''))
    #print("%s : %s" % (name, population))
    data.append((str(name), population))
#print(data)

c = (
    Map()
    .add("世界人口分布", data, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界人口"),
        visualmap_opts=opts.VisualMapOpts(max_=1500000000),
    )
    .render("population.html")
)

