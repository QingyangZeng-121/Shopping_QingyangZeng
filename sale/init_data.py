#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from faker import Faker

fake = Faker()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sale.settings")

import django

django.setup()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from product.models import ProductBrand, Product
import csv

with open('myntra_products_catalog.csv', newline="") as w:
    reader = csv.reader(w)
    no = 0
    for row in list(reader)[1:]:
        no += 1
        title = row[1].strip().replace('\u202c', '').replace('\n', '').replace('\r', '').replace('\t', '')
        price = row[4]
        img = "good_image/img.png"
        product_brand = row[2]
        product_brand_record = ProductBrand.objects.filter(name=product_brand).first()
        if not product_brand_record:
            product_brand_record = ProductBrand()
            product_brand_record.name = product_brand
            product_brand_record.save()
        record = Product()
        record.Gender = row[3]
        record.Description = row[5]
        record.PrimaryColor = row[6]
        record.title = title
        record.price = float(price)
        record.product_brand = product_brand_record
        record.inventory = fake.random_int(min=0, max=999)
        record.image = img
        record.save()
