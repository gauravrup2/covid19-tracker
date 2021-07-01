from django.shortcuts import render, HttpResponse
import requests

def home(request):
    data = True
    globalSummary = None
    countries = None
    while (data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            print("Gaurav")
            json = result.json()
            globalSummary = json['Global']
            countries = json['Countries']
            data = False
        except:
            data = True
    
    return render(request, 'index.html', {'globalSummary' : globalSummary, 'countries': countries })