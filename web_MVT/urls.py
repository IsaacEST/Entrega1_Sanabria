from django.urls import path
from web_MVT.views import *

urlpatterns = [
    path("register/", registerViews, name="register"),
    path("product/", productViews, name="product"),
    path("category/", categoryViews, name="category"),
    path("", searchItem, name="search-product"),
  

]