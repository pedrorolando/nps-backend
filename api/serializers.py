from rest_framework import serializers
from .models import Restaurant, Special

# CUSTOM SPECIAL LISTING FIELD
# This lives inside the RESTAURANT SERIALIZER and determines how each special appears as a JSON object inside the restaurant JSON object - would have just lazily used the entire SPECIAL SERIALIZER as the field, but did not like redundancy of repeating the restaurant name.

class SpecialListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {'special_id': value.id, 'title': value.title, 'category': value.category, 'day': value.day, 'every_day': value.every_day, 'created_at': value.created_at}


# SPECIAL SERIALIZER

class SpecialSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'restaurant', 'title',
                  'category', 'day', 'every_day', 'created_at']
        read_only_fields = ['created_at']
        model = Special


# RESTAURANT SERIALIZER

class RestaurantSerializer(serializers.ModelSerializer):
    # creates respective list of specials inside each response
    # Note: started out using DRF's "StringRelatedField" instead of "PrimaryKeyRelatedField" field to return the "__str__" representation, rather than the pk.
    # Then decided to use a custom listing field ("SpecialListingField" below) so I could include more info about each special (as it appears within each restaurant JSON object) than just its name (i.e. days of the week).
    # Did this instead of just using the entire special serializer class because I did not want the verbosity of including all 7 boolean fields for each day of week.
    specials = SpecialListingField(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'created_at', 'specials']
        read_only_fields = ['created_at']
