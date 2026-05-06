from rest_framework import serializers
from .models import Request, SupportingDocument

    
class SupportingDocumentSerializer(serializers.ModelSerializer):
    
    file_url = serializers.SerializerMethodField()
    file = serializers.ImageField(required=True)

    class Meta:
        model = SupportingDocument
        fields = ['id', 'request', 'file', 'file_url', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_file_url(self, obj):
        if obj.file:
            return obj.file.url
        return None
    
class RequestSerializer(serializers.ModelSerializer):

    document = SupportingDocumentSerializer(many=True, read_only=True)
    genre_display = serializers.CharField(source='get_genre_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    name = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y'], required=True)
    last_name = serializers.CharField(required=True)
    street_name = serializers.CharField(required=True)
    house_number = serializers.CharField(required=True)
    quarter = serializers.CharField(required=True)
    commune = serializers.CharField(required=True)
    telephone_number = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    profession = serializers.CharField(required=True)

    class Meta:
        model = Request
        fields = [
            'id', 'name', 'last_name', 'first_name', 'date_of_birth', 
            'genre', 'genre_display', 'street_name','house_number','quarter','commune', 'telephone_number', 
            'email', 'profession', 'status','document', 'status_display',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'status', 'created', 'updated_at']

    #validation pour le numéro phone
    def validate_telephone_number(self, value):
        if not value.startswith('+243') and not value.startswith('0'):
            raise serializers.ValidationError("Le numéro doit commencer par +243 ou 0.")
        return value