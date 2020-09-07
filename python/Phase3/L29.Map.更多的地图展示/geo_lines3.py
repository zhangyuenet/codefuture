#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


provinces = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
values = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]


myto = ["上海","北京","杭州","重庆"];
myfrom = [];
n = 0
while n < len(myto):
    myfrom.append("广州")
    n = n + 1


c = (
    Geo()
    .add_schema(maptype="china")
    .add("学生地域分布", [list(z) for z in zip(provinces, values)])
    .add(
        "geo",
        [list(z) for z in zip(myfrom, myto)],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=12, color="green"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines"),
    visualmap_opts=opts.VisualMapOpts(max_=200))
    .render("geo_lines3.html")
)
