from django.urls import path
from.import views

urlpatterns = [
    path('index1', views.home),
    path('index2',views.index2),
    path('index3',views.index3)
]