from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Main(View):
    def get(self, request):
        return render(request, 'main.html')
