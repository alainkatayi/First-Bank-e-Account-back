from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView as ApiView
from accounts.serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
#from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class RegisterView(ApiView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Utilisateur enregistré avec succès"}, status=201)
        return Response(serializer.errors, status=400)