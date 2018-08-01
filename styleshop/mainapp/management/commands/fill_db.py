from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainpage.models import Section, Category, Sex, Brand
from shoppage.models import Product
import json, os

JSON_PATH = 'mainapp/management/json_files/'

def load_from_json(file_name):

    with open(os.path.join(JSON_PATH, file_name + '.json'), 
              'r', encoding='utf-8') as file:
        return json.load(file)

class Command(BaseCommand):

    def handle(self, *args, **options):

        Section.objects.all().delete()
        Brand.objects.all().delete()
        Sex.objects.all().delete()
        
        sections = load_from_json('sections')
        for section in sections:
            add_section = Section(**section)
            add_section.save()

        brands = load_from_json('brands')
        for brand in brands:
            add_brand = Brand(**brand)
            add_brand.save()

        sexs = load_from_json('sexs')
        for sex in sexs:
            add_sex = Sex(**sex)
            add_sex.save()

        categories = load_from_json('categories')
        for category in categories:
            add_category = Category(**category)
            add_category.save()

        products = load_from_json('products')
        for product in products:
            add_product = Product(**product)
            add_product.save()
        
        if input('Create superuser? (y/n)') == 'y':
            User.objects.create_superuser(
                'admin', 'dima.gonchar.29.08.13@gmail.com', 'admin'
            )
