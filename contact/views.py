from django.shortcuts import render
from weather import Weather

import pytz
from django.utils import timezone
import pyowm
# Create your views here.

def Contact_View(request):
	weather = Weather()
	owm=pyowm.OWM('8b234a6af483751d0fc58bdae8a91fbf')
	#owm=pyowm.OWM('00408fda213390add70c0078dcb5680a') #forthisapp
	obser=owm.weather_at_place('chennai')
	w=obser.get_weather()
	wind=w.get_wind()
	temp=w.get_temperature()
	tomo=pyowm.timeutils.tomorrow()
	#weather package
	location = weather.lookup_by_location('udumalpet')
	condition = location.condition()
	t=condition.text()
	forecasts = location.forecast()
	'''for forecast in forecasts:
	    print(forecast.text())
	    print(forecast.date())
	    print(forecast.high())
	    print(forecast.low())'''

	#print(w) 
	now = timezone.now()
	context={
		'date': w,
		'wind':wind,
		'temp':temp,
		't':t,
	}	
	return render(request,"contact.html", context)