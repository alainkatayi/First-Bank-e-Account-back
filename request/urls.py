from django.urls import path
from .views import RequestCreatedView, RequestListView, TakeDecisionView

urlpatterns = [
    path('store', RequestCreatedView.as_view(), name='soumission'),
    path('index', RequestListView.as_view(), name='get-all-request'),
    path('<int:request_id>/decision', TakeDecisionView.as_view(), name='take-decision'),
]