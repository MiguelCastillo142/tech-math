from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"),name='index'),
    path('ejercicios/',TemplateView.as_view(template_name="lista.html"),name='lista'),
    path('1/',TemplateView.as_view(template_name="ejercicios/1.html"),name='1'),
    path('2/',TemplateView.as_view(template_name="ejercicios/2.html"),name='2'),
    path('3/',TemplateView.as_view(template_name="ejercicios/3.html"),name='3'),
    path('4/',TemplateView.as_view(template_name="ejercicios/4.html"),name='4'),
    path('5/',TemplateView.as_view(template_name="ejercicios/5.html"),name='5'),
 
]
