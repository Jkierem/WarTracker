from django.http import HttpResponse
import requests

def getRSS(request):
    url = 'http://content.warframe.com/dynamic/rss.php'
    request = requests.get(url)
    return HttpResponse(request)

def getWorldState(request):
    url = 'http://content.warframe.com/dynamic/worldState.php'
    request = requests.get(url)
    return HttpResponse(request)
