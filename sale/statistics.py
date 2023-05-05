#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sale.settings")

import django

django.setup()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import matplotlib.pyplot as plt
from product.models import Product

records = Product.objects.filter().all()

data = {
    "0-500": 0,
    "500-1000": 0,
    "1000-2000": 0,
    "2000-5000": 0,
    "5000+": 0
}
total = 0
for record in records:
    price = record.price
    if price < 500:
        data["0-500"] += 1
    elif 500 <= price < 1000:
        data["500-1000"] += 1
    elif 1000 <= price < 2000:
        data["1000-2000"] += 1
    elif 2000 <= price < 5000:
        data["2000-5000"] += 1
    else:
        data["5000+"] += 1
    total += 1

x = list(data.keys())
y = [round(i / total, 2) for i in list(data.values())]
p, tx, autotexts = plt.pie(x=y,
                           labels=x,
                           autopct='%.1f%%',
                           pctdistance=0.8,
                           labeldistance=1.1,
                           startangle=180,
                           radius=1.2,
                           counterclock=False,
                           wedgeprops={'linewidth': 1.5, 'edgecolor': 'red'},
                           textprops={'fontsize': 10, 'color': 'black'}
                           )
for i, a in enumerate(autotexts):
    a.set_text("{:.2%}".format(y[i]))
plt.title("price rate")
plt.savefig('static/price.jpg')
plt.show()

import plotly.express as px

# 使用px.choropleth函数画印度地图
plt = px.choropleth(locations=["IN"], scope="asia")
plt.write_image("static/india_map.png")
