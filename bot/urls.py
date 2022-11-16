from django.urls import path
from bot import views

urlpatterns=[
    path('12345',views.getCommand),
]