from django.urls import path
from .views import AnomalyListView

urlpatterns = [
    path('anomalies/', AnomalyListView.as_view(), name='anomaly-list'),
]