from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Anomaly
from .serializers import AnomalySerializer

class AnomalyListView(ListAPIView):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer