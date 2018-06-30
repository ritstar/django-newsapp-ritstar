
from django.contrib import admin
from django.urls import path, re_path, include
from ritesh import views

urlpatterns = [
    re_path('^$',views.index),
    path('rit/',include('ritesh.urls')),
    path('admin/', admin.site.urls),
    path('form/',views.form_view),
]
