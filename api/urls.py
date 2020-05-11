from django.urls import path
from .views import RestaurantList, SpecialList, RequestList


urlpatterns = [
path('restaurants/', RestaurantList.as_view()),
path('specials/', SpecialList.as_view()),
path('requests/', RequestList.as_view()),
]