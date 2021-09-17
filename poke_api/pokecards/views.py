from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed, NotAcceptable
from .serializers import CardsSerializer, TypesSerializer, ExpansionSerializer
from .models import Cards, Expansion, Types
import jwt, datetime
from rest_framework import generics
#from rest_framework.filters import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class CardsView(APIView):
    def post(self, request):
        serializer = CardsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        card = get_object_or_404(Cards.objects.filter(name=request.data.get('name',' ')).first())
        serializer = CardsSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_cards = get_object_or_404(Cards.objects.all(), pk=pk)
        data = request.data
        serializer = TypesSerializer(instance=saved_cards, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cards_saved = serializer.save()
        return Response({"success": "Card '{}' updated successfully".format(cards_saved.name)})

    def delete(self, request, pk=None):
        # Get object with this pk
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        cards = get_object_or_404(Cards.objects.all(), pk=pk)
        cards.delete()
        return Response({"message": "Cards with id `{}` has been deleted.".format(pk)},status=204)

class CreateTypesView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        serializer = TypesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        types =  get_object_or_404(Types.objects.filter(name=request.data.get('name')).first())
        serializer = TypesSerializer(types)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_types = get_object_or_404(Types.objects.all(), pk=pk)
        data = request.data
        serializer = TypesSerializer(instance=saved_types, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            types_saved = serializer.save()
        return Response({"success": "Types '{}' updated successfully".format(types_saved.types)})

    def delete(self, request, pk=None):
            # Get object with this pk
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        types = get_object_or_404(Types.objects.all(), pk=pk)
        types.delete()
        return Response({"message": "Types  with id `{}` has been deleted.".format(pk)},status=204)
    
class CreateExpansionView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        serializer = ExpansionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        expansion =  get_object_or_404(Expansion.objects.filter(name=request.data.get('name')).first())
        serializer = ExpansionSerializer(expansion)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_expansion = get_object_or_404(Expansion.objects.all(), pk=pk)
        data = request.data
        serializer = ExpansionSerializer(instance=saved_expansion, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            expansion_saved = serializer.save()
        return Response({"success": "Expansion '{}' updated successfully".format(expansion_saved.expansion)})

    def delete(self, request, pk=None):
        # Get object with this pk
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        expansion = get_object_or_404(Expansion.objects.all(), pk=pk)
        expansion.delete()
        return Response({"message": "Expansion with id `{}` has been deleted.".format(pk)},status=204)

class GetAndFindCardsView(generics.ListAPIView):

    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'is_firts_edition','rarity','price']
    search_fields = ['name', 'is_firts_edition']


