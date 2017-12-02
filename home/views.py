from django.shortcuts import render
from django.views import View
from weather import Weather
from django.http import Http404
# Create your views here.
from .forms import SearchPlace

def fun_view(request):
	form = SearchPlace()
	context={
		'form':form,
	}
	#return render(request,'index.html',context)
	return render(request,'index.html',context)



class Home_view(View):

	def get(self,request, *args , **kwargs):
		form = SearchPlace()
		context={
			'form':form,
		}
		#return render(request,'index.html',context)
		return render(request,'home.html',context)


	def post(self,request, *args , **kwargs):
		form = SearchPlace(request.POST)
		weather = Weather()
		context={
			'form':form,
		}
		template='home.html'
		if request.method == 'POST':
			if form.is_valid():
				val=form.cleaned_data.get('place')
				try:
					location = weather.lookup_by_location(val)
					condition = location.condition()
					forecasts = location.forecast()
					context={
						'form':form,
						'forecasts':forecasts,
						'va':val
					}
					return render(request,'test.html',context)
				except:
					#raise Http404
					return render(request, 'error.html')
		else:
			form = SearchPlace()
		return render(request, template, context)