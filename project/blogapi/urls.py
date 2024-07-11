from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import PostViews

route = DefaultRouter()
route.register(r'posts', PostViews, basename=PostViews)

urlpatterns = [
    path('', include(route.urls))
]