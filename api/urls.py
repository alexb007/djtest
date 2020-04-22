from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(r'applications', views.ApplicationViewSet, basename='Applications')

urlpatterns = [
    path('test/', views.TestView.as_view()),
    path('', include(router.urls)),
]
