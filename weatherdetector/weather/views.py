from django.shortcuts import render
import json # when we request an api it will give response in json format
import urllib.request


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        encoded_city = urllib.parse.quote(city)
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+encoded_city+'&units=metric&appid=51c1fe13e7fac3ddc9650e9f2d0b8109').read() #after ? we pass parameters and q is query and = is used coz we are passing parameters
        json_data = json.loads(res)
        # Unit system: 'standard', 'metric', or 'imperial' Default to Kelvin i.e standard
        data  = {
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+ ' '+str(json_data['coord']['lat']), # lon=longitude and lat=latitude
            "temp":str(json_data['main']['temp'])+'°C',
            "pressure":str(json_data['main']['pressure'])+'hPa',
            "humidity":str(json_data['main']['humidity'])+'%',
        } 
    else:
        city = ''
        data = {}  
          
    return render(request, 'index.html', {'city':city, 'data':data})
