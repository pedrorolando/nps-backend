from django.urls import path
from .views import RestaurantList, SpecialList


urlpatterns = [
path('restaurants/', RestaurantList.as_view()),
path('specials/', SpecialList.as_view()),
]