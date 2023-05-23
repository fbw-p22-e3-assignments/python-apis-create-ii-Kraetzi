#new - whole script added by instructor
from django.urls import include, path
from .views import ProductList, ProductCreate, ProductDelete, ProductDetail


urlpatterns = [
    path('', ProductList.as_view()),
    path('create/', ProductCreate.as_view(), name='create-product'),
    path('<uuid:id>/', ProductList.as_view(), name='retrieve-product'),
    path('getproduct/<name>/', ProductDetail.as_view(), name='update-product'),
    path('delete/<uuid:id>/', ProductDelete.as_view(), name='delete-product')

]

