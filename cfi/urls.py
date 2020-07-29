from cfi import views
from django.urls import path

app_name = 'cfi'

urlpatterns = [
    path('', views.index, name='index'),
]