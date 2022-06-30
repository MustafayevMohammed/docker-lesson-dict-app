from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import View
import requests
# Create your views here.

class HomePageView(View):
    
    def get(self,request ,*args, **kwargs):
        q = request.GET.get("q")
        if q == None:
            print("bosdur")
        else:
            try:
                url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{q}"
                response = requests.get(url)
                word = response.json()[0]["word"]
                return redirect("dictionary:detail",word)
            except KeyError:
                return redirect("/")
        return render(request, "home.html")


class DetailPageView(View):
    
    def get(self,request,word ,*args, **kwargs):
        print(word)
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        
        instance = response.json()[0]

        
        context = {
            "word" : word,
        }

        try:
            text = instance["phonetics"][1]["text"]
        except KeyError:
            print("yoxdur")
        else:
            context["text"] = text

        try:
            audio = instance["phonetics"][0]["audio"]
        except KeyError:
            print("yoxdur")
        else:
            context["audio"] = audio

        try:
            example = instance["meanings"][0]["definitions"][0]["example"]
        except KeyError:
            print("yoxdur")
        else:
            context["example"] = example

        try:
            definition = instance["meanings"][0]["definitions"][0]["definition"]
        except KeyError:
            print("yoxdur")
        else:
            context["definition"] = definition


        try:
            origin = instance["origin"]
        except KeyError:
            print("yoxdur")
        else:
            context["origin"] = origin


        return render(request, "detailofword.html",context)