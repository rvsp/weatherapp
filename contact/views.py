from django.shortcuts import render

# Create your views here.

def Contact_View(request):
	return render(request,"contact.html")