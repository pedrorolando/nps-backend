from rest_framework import serializers
from .models import Restaurant, Special


# CUSTOM SPECIAL LISTING FIELD
# This is called inside of the RESTAURANT SERIALIZER and overrides how each restaurant JSON object portrays its specials.
# Made this because I didn't want the verbosity of having all 7 days in every restaurant object.
class SpecialListingField(serializers.RelatedField):
    def to_representation(self, value):
        days = []
        if value.monday == True:
            days.append('monday')
        if value.tuesday == True:
            days.append('tuesday')
        if value.wednesday == True:
            days.append('wednesday')
        if value.thursday == True:
            days.append('thursday')
        if value.friday == True:
            days.append('friday')
        if value.saturday == True:
            days.append('saturday')
        if value.sunday == True:
            days.append('sunday')
        
        if value.every_day == True:
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        # final nested JSON object representing each special in every restaurant object:
        return {'special_id': value.id, 'title' : value.title, 'every_day': value.every_day, 'days' : days}

# RESTAURANT SERIALIZER

class RestaurantSerializer(serializers.ModelSerializer):
    # creates respective list of specials inside each response
    # Note: started out using DRF's "StringRelatedField" instead of "PrimaryKeyRelatedField" field to return the "__str__" representation, rather than the pk. 
    # Then decided to use a custom listing field ("SpecialListingField" below) so I could include more info about each special (as it appears within each restaurant JSON object) than just its name (i.e. days of the week).
    # Did this instead of just using the entire special serializer class because I did not want the verbosity of including all 7 boolean fields for each day of week.
    specials = SpecialListingField(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'specials', 'created_at']
        read_only_fields = ['created_at']


# SPECIAL SERIALIZER

class SpecialSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'restaurant', 'title', 'category', 'every_day', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'created_at']
        read_only_fields = ['created_at']
        model = Special