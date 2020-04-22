from django.urls import path, include
from . import views

app_name='appy'
urlpatterns = [
    path('', views.front_page_view, name='front_page'),
]