from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.http import JsonResponse

from multiprocessing import Queue, Process

def query_prolog(data, output):
	from pyswip.prolog import Prolog
	from pyswip.easy import call, Functor, registerForeign

	prolog = Prolog() # handle for Prolog interpreter

	# Fetch Prolog inputs
	distance = str(data[0])
	price = str(data[1])
	type = str(data[2])
	veg_options = str(data[3])

	# open KB file from static location
	prolog.consult('static/KB.pl')

	# assert knowledge at top of KB
	prolog.asserta("veg_options("+veg_options+")")
	prolog.asserta("distance("+distance+")")
	prolog.asserta("price("+price+")")
	prolog.asserta("type("+type+")")

	# get results from KB
	results = [sol['X'] for sol in prolog.query("recommendation(X).", maxresult=1)]

	if results:
		output.put(("You should eat at " + results[0] + "!"))
	else:
		output.put(("No restaurant could be identified!"))

def home(request):
	return render(request, "index.html", {})

def query_restaurant(request):
	distance = request.POST.get('distance')
	price = request.POST.get('price')
	type_restaurant = request.POST.get('type')
	ifveg = request.POST.get('veg')

	data = [distance, price, type_restaurant, ifveg]

	# create Prolog parallel process
	output = Queue()
	process = Process(target=query_prolog, args=(data, output, ))
	process.start()
	process.join()

	# get results from Prolog subprocess
	results = output.get()

	result = {
		"restaurant_name": results
	}
	return JsonResponse(result)
