from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests

class AppView(View):
    def get(self, request):
        url = "https://dn8mlk7hdujby.cloudfront.net/interview/insurance/58"
        response = requests.get(url)
        data = response.json()

        insurance = data.get('insurance', {})

        return render(request, 'app_interface.html', {'insurance': insurance})
