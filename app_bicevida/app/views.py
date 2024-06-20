from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

#obtenemos los datos entregados en el endpoint con la función get
class AppView(APIView):
    def get(self, request):
        response = requests.get('https://dn8mlk7hdujby.cloudfront.net/interview/insurance/58')
        return Response(response.json())

