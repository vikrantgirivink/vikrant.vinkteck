from django.contrib import admin
from django.urls import path
from customers import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', views.customers_list,name='customers_list'),
    url('', views.customers_detail,name='customer_details'),
]
