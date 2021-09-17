from rest_framework import serializers
from .models import Cards, Types, Expansion


class TypesSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        return Types.objects.create(**validated_data)

    class Meta:
        model = Types
        fields = ['types','pk']
        extra_kwargs = {
            'types': {'required': True}
        }

class ExpansionSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        return Expansion.objects.create(**validated_data)
    
    class Meta:
        model = Expansion
        fields = ['expansion','pk']
        extra_kwargs = {
            'expansion': {'required': True}
        }

class CardsSerializer(serializers.HyperlinkedModelSerializer):
    types = TypesSerializer(read_only=True)
    expansion = ExpansionSerializer(read_only=True)
    
    def create(self, validated_data):
        return Cards.objects.create(**validated_data)
    class Meta:
        model = Cards
        fields = ['name', 'hp', 'types','start_date','expansion','is_firts_edition','rarity','price','image_cards','pk']
        extra_kwargs = {
            'name': {'required': True},
            'hp': {'required': True},
            'is_firts_edition': {'required': True},
            'price': {'required': True},
            'rarity': {'required': True},
        }