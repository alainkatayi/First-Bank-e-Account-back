from rest_framework import status
from rest_framework.response import Response
from .models import SupportingDocument
from .serializers import RequestSerializer
from rest_framework.views import APIView
from rest_framework.permissions import  AllowAny, IsAuthenticated
from rest_framework import status
from django.db import transaction
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView
from .models import Request
from abstracts_models.permission import IsAdminOrAgent
from abstracts_models.pagination import Pagination
# Create your views here.
class RequestCreatedView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    def post(self,request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES.get('file')
            if not file:
                return Response(
                    {"error": "La pièce d'identité est obligatoire."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                #on utilise une transaction pour eviter de creer une request, si l'enregistrement de l'image echoue
                with transaction.atomic():
                    request_instance = serializer.save()
                    SupportingDocument.objects.create(
                        request=request_instance,
                        file=file
                    )
                return Response({
                    "message": f"Cher client {request_instance.first_name}, votre demande a été reçue avec succès.",
                    "detail": "Nous reviendrons vers vous dans un bref délai pour vous informer du statut de votre dossier."
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(
                    {"error": str(e)}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestListView(ListAPIView):
    queryset = Request.objects.all().order_by('-created_at')
    serializer_class = RequestSerializer
    #on verifie l'authentifiation et le role
    permission_classes = [IsAuthenticated, IsAdminOrAgent]
    pagination_class = Pagination