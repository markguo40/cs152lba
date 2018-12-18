from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.http import JsonResponse

from multiprocessing import Queue, Process

def run_unification(data, output):
	from pyswip.prolog import Prolog
	from pyswip.easy import call, Functor, registerForeign

	prolog = Prolog() # handle for Prolog interpreter

	# Prolog inputs
	distance = str(data[0])
	price = str(data[1])
	type = str(data[2])
	veg_options = str(data[3])

	# open KB file from static location
	prolog.consult('static/KB_alt.pl')

	print("distance("+distance+")")

	# assert knowledge at top of KB
	prolog.asserta("veg_options("+veg_options+")")
	prolog.asserta("distance("+distance+")")
	prolog.asserta("price("+price+")")
	prolog.asserta("type("+type+")")

	# get results from KB
	results = [sol for sol in prolog.query("recommendation(X).", maxresult=1)]
	# print([sol for sol in prolog.query("recommendation(X).", maxresult=1)])
	# for soln in prolog.query("recommendation(X).", maxresult=1):
	#     resultcount = resultcount + 1
	#     output.put(("You should eat at " + soln['X'] + "!"))
	#

	# if not results:
	# 	output.put(("No restaurant could be identified!"))
	# else:
	# 	print(results)
	output.put((results))

def home(request):
	return render(request, "index.html", {})

def query_restaurant(request):
	distance = request.POST.get('distance')
	price = request.POST.get('price')
	type_restaurant = request.POST.get('type')
	ifveg = request.POST.get('veg')

	data = [distance, price, type_restaurant, ifveg]

	output = Queue()

	process = Process(target=run_unification, args=(data, output, ))
	process.start()
	process.join()


	results = output.get()

	# print(results)

	result = {
		"restaurant_name": results #change value here
	}
	return JsonResponse(result)
