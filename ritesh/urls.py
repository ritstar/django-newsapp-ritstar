from django.urls import path, re_path
from ritesh import views

urlpatterns = [
    re_path('^$',views.index),
]