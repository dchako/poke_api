from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAcceptable


class HomeView(APIView):
    def get(self, request):
        name = "Algunos methodos necesitan login"
        return Response({"success": "API Poke Cards is alive but '{}'".format(name)})