from django.shortcuts import render
import json
import requests


# Create your views here.

def home(request):

    if request.method == 'POST':
        city = request.POST.get('city')

        api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=13ad4049324a3b0feac3260fa3a4a956&lang=fa')

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = 'Error...'

        return render(request , 'home.html' , {'api':api})

    else:
        
        api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=tehran&appid=13ad4049324a3b0feac3260fa3a4a956&lang=fa')

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = 'Error...'

        return render(request , 'home.html' , {'api':api})

def about(request):

    return render(request , 'about.html' , {})