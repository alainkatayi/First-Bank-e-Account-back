from django.urls import path
from .views import RequestCreatedView, RequestListView

urlpatterns = [
    path('store', RequestCreatedView.as_view(), name='soumission'),
    path('index', RequestListView.as_view(), name='get-all-request'),
]