# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.uy, name='uy'), # Bosh sahifa
	path('kirish/', views.kirish, name='kirish'), # Kirish uchun sahifa
	path('hisob-yaratish/', views.ro, name='ro'), # Ro'yxatdan o'tish
	path('chiqish/', views.chiqish, name='chiqish'), # Chiqib ketish
]