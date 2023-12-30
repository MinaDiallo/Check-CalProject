from django.urls import path
from .views import *

urlpatterns = [
    path('foods', FoodsView.as_view(), name= 'listFoods'),
    path('foodsRegister', CreateFoodsView.as_view())
]
