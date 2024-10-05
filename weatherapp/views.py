from django.shortcuts import render, HttpResponse
import requests
import datetime
from django.contrib import messages


def home(request):
   
    if "city" in request.POST:
        city = request.POST["city"]
    else:
        city = "Jodhpur"

   
    url = "https://api.openweathermap.org/data/2.5/weather"
   
    PARAMS = {
        "q": city, 
        "appid": "f47fd885d4b564b4503b45bad25309cb",  
        "units": "metric"
    }

    try:
        
        response = requests.get(url, params=PARAMS)
        data = response.json()

       
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]
        date = datetime.date.today()

     
        return render(
            request,
            "index.html",
            {
                "description": description,
                "icon": icon,
                "city": city,
                "temp": temp,
                "date": date,
            },
        )
    except KeyError:
        
        messages.error(request, "Entered city is not available")
        date = datetime.date.today()

       
        
