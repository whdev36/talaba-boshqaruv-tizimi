# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.uy, name='uy'), # Bosh sahifa
]