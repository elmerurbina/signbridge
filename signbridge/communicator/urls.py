from django.urls import path, re_path
from . import views
from .consumers import SignBridgeConsumer

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'ws/signbridge/', SignBridgeConsumer.as_asgi()),
    path('video_feed/', views.video_feed, name='video_feed'),
]
