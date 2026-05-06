from django.db import models
from abstracts_models.soft_delete_model import SoftDeleteModel
from abstracts_models.time_stamped_model import TimeStampedModel


class Request(TimeStampedModel ,SoftDeleteModel):

    genre_choice = [
        ('H','Homme'),
        ('F', 'Femme')
    ]
    status_choice = [
        ('PENDING','pending'),
        ('APPROVED', 'approved'),
        ('REJECTED', 'rejected')
    ]
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    genre = models.CharField(max_length=20, choices=genre_choice, default='H')
    street_name = models.CharField(max_length=250, null=False)
    house_number = models.CharField(max_length=100, null=False)
    quarter = models.CharField(max_length=200, null=False )
    commune=models.CharField(max_length=200, blank=True, null=False)
    telephone_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=False)
    profession = models.CharField(max_length=150, null=False)
    status = models.CharField(max_length=20, choices=status_choice, default= 'PENDING')

class SupportingDocument(SoftDeleteModel, TimeStampedModel):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='document')
    file = models.ImageField(upload_to='identity_docs/%Y/%m/%d/')


    


