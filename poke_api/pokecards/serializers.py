from rest_framework import serializers
from .models import Cards, Types, Expansion


class UserSerializer(serializers.HyperlinkedModelSerializer):
    types = TypesSerializer(read_only=True)
    expansion = ExpansionSerializer(read_only=True)
    class Meta:
        model = Cards
        fields = ['id', 'name', 'hp', 'types','start_date','expansion','is_firts_edition','rarity','price','image_cards']
        extra_kwargs = {
            'name': {'required': True},
            'hp': {'required': True},
            'is_firts_edition': {'required': True},
            'price': {'required': True},
            'rarity': {'required': True},
        }

class TypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Types
        fields = ['types',]
        extra_kwargs = {
            'types': {'required': True}
        }

class ExpansionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expansion
        fields = ['expansion',]
        extra_kwargs = {
            'expansion': {'required': True}
        }

