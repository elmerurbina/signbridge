from django.urls import path
from .views import HandSignView, SpeechToSignView, SystemStatusView

urlpatterns = [
    path('hand-sign/', HandSignView.as_view(), name='hand-sign'),
    path('speech-to-sign/', SpeechToSignView.as_view(), name='speech-to-sign'),
    path('status/', SystemStatusView.as_view(), name='system-status'),
]
