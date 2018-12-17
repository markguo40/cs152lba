from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.http import JsonResponse

from multiprocessing import Queue, Process

def run_unification(data, output):
	from pyswip.prolog import Prolog
	from pyswip.easy import call, Functor, registerForeign

	prolog = Prolog() # handle for Prolog interpreter

	# open KB file from static location
	prolog.consult('static/KB.pl')

	retractall = Functor("retractall")
	known = Functor("known", 3)

	# Prolog functions

	# distance or price
	def read_py_menu3(A,V,Y):
		if str(A) == 'distance':
			Y.unify(str(data[0]))
		else:
			Y.unify(str(data[1]))
		return True

	# restaurant type
	def read_py_menu8(A,V,Y):
	    Y.unify(str(data[2]))
	    return True

	# veg options
	def read_py(A,V,Y):
		if str(A) == 'veg_options':
			Y.unify(str(data[3]))
		return True

	read_py.arity = 3
	read_py_menu8.arity = 3
	read_py_menu3.arity = 3

	registerForeign(read_py)
	registerForeign(read_py_menu8)
	registerForeign(read_py_menu3)

	call(retractall(known))
	resultcount = 0
	for soln in prolog.query("recommendation(X).", maxresult=1):
	    resultcount = resultcount + 1
	    output.put(("You should eat at " + soln['X'] + "!"))

	if not resultcount:
		output.put(("No restaurant could be identified!"))

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

	print(results)
	# start thread Pool on which to run Prolog interpreter
	# pool = Pool(None, initialise)

	# pool.apply(run_unification, (data,))
	#
	# pool.close()
	# pool.join()
	#
	# results = [r.get() for r in results]
	# print(results)

	result = {
		"restaurant_name": "None" #change value here
	}
	return JsonResponse(result)
