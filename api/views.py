from rest_framework import generics
from .models import Restaurant, Special
from .serializers import RestaurantSerializer, SpecialSerializer

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class SpecialList(generics.ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
