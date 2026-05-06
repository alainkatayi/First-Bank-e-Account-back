from rest_framework import status
from rest_framework.response import Response
from .models import SupportingDocument
from .serializers import RequestSerializer, DecisionSerializer
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

#class pour la prise de decision sur une request(demande d'ouverture)
#deux cas possible: refus ou acceptation
class TakeDecisionView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrAgent]
    def post(self, request, request_id):
        try:
            #la recupere la requete à traiter
            request_to_process = Request.objects.get(id=request_id)
        except Request.DoesNotExist:
            #si la requette n'est pas trouvé
            return Response({"error": "Demande introuvable"}, status=status.HTTP_404_NOT_FOUND)
        #on verifie si une decision a deja ete rendu sur cette demande
        if hasattr(request_to_process, 'decision'):
            return Response({"error": "Une décision a déjà été rendue pour ce dossier"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DecisionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    decision = serializer.save(
                        request=request_to_process,
                        agent=request.user
                    )
                    request_to_process.status = decision.decision_type
                    request_to_process.save()
                return Response({"message": "Décision enregistrée avec succès"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)