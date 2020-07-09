from django.urls import path

from .views import ProductList, ProductDetail

urlpatterns = [
	path('', ProductList.as_view()),
	path('<int:product_id>', ProductDetail.as_view()),
]
