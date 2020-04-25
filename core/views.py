from django.shortcuts import render,redirect
import requests
from .models import *

# Create your views here.


def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7b0d6b53ad53c51f884baaef3278eff9'
    userid = request.session.get('userid')
    if request.method=="POST":
        
        city = request.POST['city']
        test= requests.get(url.format(city)).json()
        if test['cod']=="404":
            error="Location not found"
        else:
            error= False
            citydata = City(city=city,userid=userid)
            citydata.save()
    else:
        error = False
    
    query_set = City.objects.filter(userid=userid).order_by('id')
    ordered_query = query_set.reverse()[:8]
    cities = []
    for citys in ordered_query:
        r= requests.get(url.format(citys.city)).json()
        weath = {
            'city':r['name'],
            'temp' : r['main']['temp'],
            'pressure':r['main']['pressure'],
            'temp_min':r['main']['temp_min'],
            'temp_max':r['main']['temp_max'],
            'des' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }
        cities.append(weath)
    if cities:
        city1 = cities[0]
    else:
        city1 = None
    return render(request,'home.html',{'data':city1,'alldata':cities,'error':error})
    
def logout(request):
    request.session['userid']=None
    return redirect('http://127.0.0.1:8000/')     
