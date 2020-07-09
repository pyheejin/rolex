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
			collection = Collection.objects.get(id=product['collection_id'])
			size = Size.objects.get(id=product['size_id'])
			material = Material.objects.get(id=product['material_id'])

			data = {
				'id':product['id'],
				'collection':collection.name,
				'size':size.size,
				'material':material.name,
				'name':product['name'],
				'thumbnail':product['thumbnail'],
			}
			return JsonResponse({'data':data}, status=200)
		return JsonResponse({'message':'No Data'}, status=400)


class ProductDetail(View):
	def get(self, request, product_id):
		products = Product.objects.filter(id=product_id)
		features = Feature.objects.filter(product_id=product_id).values()
		result = []
		for product in products:
			data = {
				'id':product.id,
				'category':product.category.name,
				'collection':product.collection.name,
				'size':product.size.size,
				'material':product.material.name,
				'name':product.name,
				'header_image':product.header_image,
				'header_background_image':product.header_background_image,
				'description':product.description,
				'sub_description':product.sub_description,
				'price':product.price,
				'middle_thumbnail_image':product.middle_thumbnail_image,
				'middle_image':product.middle_image,
				'middle_title':product.middle_title,
				'middle_sub_title':product.middle_sub_title,
				'middle_description':product.middle_description,
			}
			result.append(data)

		for feature in features:
			feature_data = {
				'feature_title':feature['title'],
				'feature_sub_title':feature['sub_title'],
				'feature_description':feature['description'],
				'feature_thumbnail_image':feature['thumbnail_image'],
				'feature_image':feature['image']
			}
			result.append(feature_data)
		return JsonResponse({'data':result}, status=200)

