from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	             path('FastenerDetection.html', views.FastenerDetection, name="FastenerDetection"), 
	             path('FastenerDetectionAction', views.FastenerDetectionAction, name="FastenerDetectionAction"),
		       	       
]
