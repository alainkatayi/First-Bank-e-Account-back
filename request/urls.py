from django.urls import path
from .views import RequestCreatedView

urlpatterns = [
    path('store', RequestCreatedView.as_view(), name='soumission'),
]