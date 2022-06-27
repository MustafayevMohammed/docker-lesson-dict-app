from django.shortcuts import render
from django.views.generic import View
import requests
# Create your views here.

class HomePageView(View):
    
    def get(self,request ,*args, **kwargs):
        return render(request, "home.html")