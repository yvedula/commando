from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^index', views.index),
    url(r'^add-item', views.add_item),
   
]
