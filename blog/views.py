from django.shortcuts import render
import requests 
import json


# Create your views here.
def list_page_view(request):
    data = True
    result = None
    globalSummary = None
    countries = None

    while (data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            globalSummary = json['Global']
            countries = json['Countries']
            data = False
        except Exception as e:
            print(e)
            data = True

    context = {
        'title': 'List View',
        'globalSummary':globalSummary,
        'countries':countries
    }

    return render(request, 'blog/list_page.html',  context)




