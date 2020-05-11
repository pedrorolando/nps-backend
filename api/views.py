from rest_framework import generics, permissions
from .models import Restaurant, Special, Request
from .serializers import RestaurantSerializer, SpecialSerializer, RequestSerializer

class RestaurantList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) 
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class SpecialList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) 
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

class RequestList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,) 
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
