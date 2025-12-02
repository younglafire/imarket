from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('guitar/<int:pk>/', views.guitar_detail, name='guitar_detail'),
    path('amp/<int:pk>/', views.amp_detail, name='amp_detail'),
    path('fuzz/<int:pk>/', views.fuzz_detail, name='fuzz_detail'),
]