import json

from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import (Category, Collection, Product, Feature, Size, Material, Bezel,
		Bracelet, Dial)

class ProductList(View):
	def get(self, request):
		size = request.GET.get('size', None)
		material = request.GET.get('material', None)
		bezel = request.GET.get('bezel', None)
		bracelet = request.GET.get('bracelet', None)
		dial = request.GET.get('dial', None)
		
		product_filter = {
			'size__size':size,
			'material__name':material,
			'bezel__name':bezel,
			'bracelet__name':bracelet,
			'dial__name':dial
		}

		if size == None:
			del(product_filter['size__size'])
		if material == None:
			del(product_filter['material__name'])
		if bezel == None:
			del(product_filter['bezel__name'])
		if bracelet == None:
			del(product_filter['bracelet__name'])
		if dial == None:
			del(product_filter['dial__name'])
			
		products = Product.objects.filter(**product_filter).values()
		
		for product in products:
			category = Category.objects.get(id=product['category_id'])
			collection = Collection.objects.get(id=product['collection_id'])
			size = Size.objects.get(id=product['size_id'])
			material = Material.objects.get(id=product['material_id'])
			bezel = Bezel.objects.get(id=product['bezel_id'])
			bracelet = Bracelet.objects.get(id=product['bracelet_id'])
			dial = Dial.objects.get(id=product['dial_id'])
			
			data = {
				'id':product['id'],
				'category':category.name,
				'collection':collection.name,
				'size':size.size,
				'material':material.name,
				'bezel':bezel.name,
				'bracelet':bracelet.name,
				'dial':dial.name,
				'name':product['name'],
				'thumbnail':product['thumbnail'],
				'header_image':product['header_image'],
				'header_background_image':product['header_background_image'],
				'description':product['description'],
				'sub_description':product['sub_description'],
				'price':product['price'],
				'middle_thumbnail_image':product['middle_thumbnail_image'],
				'middle_image':product['middle_image'],
				'middle_title':product['middle_title'],
				'middle_sub_title':product['middle_sub_title'],
				'middle_description':product['middle_description']
			}
			return JsonResponse({'data':data}, status=200)
		return JsonResponse({'message':'No Data'}, status=400)
