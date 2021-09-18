from django.test import TestCase

# Create your tests here.
from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .serializers import CardsSerializer, TypesSerializer, ExpansionSerializer
from .models import Cards, Expansion, Types

client = Client()

class TypesTest(TestCase):
    
    def setUp(self):
        Types.objects.create(
            type='Fuego')
        Types.objects.create(
            type='Aire')
        Types.objects.create(
            type='Tierra')
        Types.objects.create(
            type='Agua')

    def test_types_name(self):
        types_fuego = Types.objects.get(type='Fuego')
        types_aire = Types.objects.get(type='Aire')
        types_tierra = Types.objects.get(type='Tierra')
        types_agua = Types.objects.get(type='Agua')
        self.assertEqual(
            types_fuego.type, "Fuego")
        self.assertEqual(
            types_aire.type, "Aire")
        self.assertEqual(
            types_tierra.type, "Tierra")
        self.assertEqual(
            types_agua.type, "Agua")

class ExpansionTest(TestCase):
    
    def setUp(self):
        Expansion.objects.create(
            expansion="Jungle")
        Expansion.objects.create(
            expansion="Fossil")

    def test_expansion_name(self):
        expansion_jungle = Expansion.objects.get(expansion='Jungle')
        expansion_fossil = Expansion.objects.get(expansion='Fossil')
        self.assertEqual(
            expansion_jungle.expansion, "Jungle")
        self.assertEqual(
            expansion_fossil.expansion, "Fossil")
        
class CardsTest(TestCase):
    
    def setUp(self):
        Ex = Expansion.objects.create(
            expansion="Jungle")
        Ty = Types.objects.create(
            type='Fuego')
        Cards.objects.create(
            name ="Pikachu",
            hp = 110,
            types = Ty.pk,
            expansion = Ex.pk,
            is_firts_edition = True
            )
        Cards.objects.create(
            name='Charizard', hp = 120,
            types = Ty.pk,
            expansion = Ex.pk,
            is_firts_edition = False)

    def test_cards_name(self):
        cards_charizard = Cards.objects.get(name='Charizard')
        cards_pikachu = Cards.objects.get(name='Pikachu')
        self.assertEqual(
            cards_charizard.name, "Charizard")
        self.assertEqual(
            cards_pikachu.name, "Pikachu")
        


class CreateNewCardsTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            "name":"pikachuws",
            "hp": 129,
            "is_firts_edition":False,
            "rarity":"COMUN",
             "price":1.2,
            "expansion_id": 1,
             "types_id": 1
        }
        self.payload_type = {
            "type":"Fuego"
        }
        self.payload_expansion = {
            "expansion":"Jungle"
        }
        self.invalid_payload = {
            "name":"pikachuws",
            "hp": 129,
            "is_firts_edition":False,
            "rarity":"COMUNs",
            "price":1.2,
            "expansion_id": 1,
            "types_id": 1
        }

    def test_create_valid_cards(self):
        typ = client.post(
            reverse('post_types_create'),
            data=json.dumps(self.payload_type),
            content_type='application/json'
        ).json()
        exp = client.post(
            reverse('post_expansion_create'),
            data=json.dumps(self.payload_expansion),
            content_type='application/json'
        ).json()
        self.valid_payload['type_id'] = int(typ.get("pk"))
        self.valid_payload['expansion_id'] = int(exp.get("pk"))
        response = client.post(
            reverse('post_cards_create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_cards(self):
        response = client.post(
            reverse('post_cards_create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
