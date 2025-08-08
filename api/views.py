from rest_framework.views import APIView
from rest_framework.response import Response

class HandSignView(APIView):
    def get(self, request):
        return Response({"message": "HandSign endpoint working"})

class SpeechToSignView(APIView):
    def get(self, request):
        return Response({"message": "SpeechToSign endpoint working"})

class SystemStatusView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
