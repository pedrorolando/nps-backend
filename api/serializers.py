from rest_framework import serializers
from .models import Restaurant, Special

# SPECIAL SERIALIZER

class SpecialSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'restaurant', 'title', 'category', 'day', 'every_day', 'created_at']
        read_only_fields = ['created_at']
        model = Special


# RESTAURANT SERIALIZER

class RestaurantSerializer(serializers.ModelSerializer):
    # creates respective list of specials inside each response
    # Note: started out using DRF's "StringRelatedField" instead of "PrimaryKeyRelatedField" field to return the "__str__" representation, rather than the pk. 
    # Then decided to use a custom listing field ("SpecialListingField" below) so I could include more info about each special (as it appears within each restaurant JSON object) than just its name (i.e. days of the week).
    # Did this instead of just using the entire special serializer class because I did not want the verbosity of including all 7 boolean fields for each day of week.
    specials = SpecialSerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'created_at', 'specials']
        read_only_fields = ['created_at']


