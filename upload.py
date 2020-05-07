import os
import django
import csv
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rolex.settings")
django.setup()


from product.models import *


CSV_PATH = './csv/size.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Size.objects.create(
            size = row['size']
        )

CSV_PATH = './csv/material.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Material.objects.create(
            name = row['name'],
            image = row['image'],
            background_image = row['background_image']
        )

CSV_PATH = './csv/bezel.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Bezel.objects.create(
            material  = Material.objects.get(id = row['material']),
            name = row['name'],
            image = row['image']
        )


CSV_PATH = './csv/bracelet.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Bracelet.objects.create(
            material  = Material.objects.get(id = row['material']),
            name = row['name'],
            image = row['image']
        )


CSV_PATH = './csv/dial.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Dial.objects.create(
            material  = Material.objects.get(id = row['material']),
            name = row['name'],
            image = row['image']
        )


CSV_PATH = './csv/category.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Category.objects.create(
            name = row['name']
        )

CSV_PATH = './csv/collection.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Collection.objects.create(
			category = Category.objects.get(id=row['category']),
            name = row['name']
        )


CSV_PATH = './csv/product.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Product.objects.create(
			category = Category.objects.get(id=row['category']),
			collection = Collection.objects.get(id=row['collection']),
			size = Size.objects.get(id=row['size']),
			material = Material.objects.get(id=row['material']),
			bezel = Bezel.objects.get(id=row['bezel']),
			bracelet = Bracelet.objects.get(id=row['bracelet']),
			dial = Dial.objects.get(id=row['dial']),
			name = row['name'],
			thumbnail = row['thumbnail'],
			header_image = row['header_image'],
			header_background_image = row['header_background_image'],
			description = row['description'],
			sub_description = row['sub_description'],
			price = row['price'],
			middle_thumbnail_image = row['middle_thumbnail_image'],
			middle_image = row['middle_image'],
			middle_title = row['middle_title'],
			middle_sub_title = row['middle_sub_title'],
			middle_description = row['middle_description']
        )


CSV_PATH = './csv/feature.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Feature.objects.create(
			product = Product.objects.get(id=row['product']),
            title = row['title'],
			sub_title = row['sub_title'],
			description = row['description'],
			thumbnail_image = row['thumbnail_image'],
			image = row['image']
        )
