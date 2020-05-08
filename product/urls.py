from django.urls import path

from .views import ProductList, ProductDetail

urlpatterns = [
	path('/list', ProductList.as_view()),
	path('/detail/<int:product_id>', ProductDetail.as_view()),
]
