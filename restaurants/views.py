from django.shortcuts import render
from django.http import JsonResponse

from pyswip.prolog import Prolog
from pyswip.easy import *

def home(request):
	return render(request, "index.html", {})


def query_restaurant(request):
	distance = request.POST.get('distance')
	price = request.POST.get('price')
	type_restaurant = request.POST.get('type')
	ifveg = request.POST.get('veg')

	print(distance)
	print(price)
	print(type_restaurant)
	print(ifveg)
	# Write code here:

	result = {
		"restaurant_name": "None" #change value here
	}
	return JsonResponse(result)
