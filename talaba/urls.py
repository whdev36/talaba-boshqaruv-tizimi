# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.uy, name='uy'), # Bosh sahifa
	path('kirish/', views.kirish, name='kirish'), # Kirish uchun sahifa
]