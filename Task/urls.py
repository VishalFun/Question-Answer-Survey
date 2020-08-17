from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('question/',views.question,name='question'),
]
