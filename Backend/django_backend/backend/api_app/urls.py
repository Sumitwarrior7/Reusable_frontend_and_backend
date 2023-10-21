from django.urls import path
from . import views

urlpatterns = [
    path('get-response/', views.GetResponse, name='get_response'),
]