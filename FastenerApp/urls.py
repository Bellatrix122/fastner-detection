from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("index.html", views.index, name="index"),
    path('FastenerDetection.html', views.FastenerDetection, name="FastenerDetection"),
    path('FastenerDetectionAction', views.FastenerDetectionAction, name="FastenerDetectionAction"),
]