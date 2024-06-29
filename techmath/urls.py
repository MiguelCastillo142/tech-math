from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"),name='index'),
    path('ejercicios/',TemplateView.as_view(template_name="lista.html"),name='lista'),
    path('1/',TemplateView.as_view(template_name="ejercicios/1.html"),name='1'),
]
