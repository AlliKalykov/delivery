from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_order, name='index'),
    path('order-detail/<int:id>/', views.order_detail, name='order_detail'),
    path('order-list/', views.list_order, name='order_list'),
]
