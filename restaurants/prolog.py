from pyswip.prolog import Prolog
from pyswip.easy import *

# prolog = Prolog() # Global handle to interpreter
#
# retractall = Functor("retractall")
# known = Functor("known", 3)
#
# # Define foreign functions for getting user input and writing to the screen
# def write_py(X):
#     print(str(X))
#     sys.stdout.flush()
#     return True
#
# def read_py(A,V,Y):
#     Y.unify(input(str(A) + " is " + str(V) + "?"))
#     return True
#
# def read_py_menu8(A,V,Y):
#     ans = input("Choose a " + str(A) + ". Select 1 for " + str(V[0]) + ', 2 for ' + str(V[1]) + ', 3 for ' + str(V[2]) + ', 4 for ' + str(V[3]) + ', 5 for ' + str(V[4]) + ', 6 for ' + str(V[5]) + ', 7 for ' + str(V[6]) + ', or 8 for ' + str(V[7]) + ".")
#     if ans == '1':
#         Y.unify(str(V[0]))
#     elif ans == '2':
#         Y.unify(str(V[1]))
#     elif ans == '3':
#         Y.unify(str(V[2]))
#     elif ans == '4':
#         Y.unify(str(V[3]))
#     elif ans == '5':
#         Y.unify(str(V[4]))
#     elif ans == '6':
#         Y.unify(str(V[5]))
#     elif ans == '7':
#         Y.unify(str(V[6]))
#     elif ans == '8':
#         Y.unify(str(V[7]))
#     else:
#         Y.unify('Choose a number from 1 to 8!')
#     return True
#
# def read_py_menu3(A,V,Y):
#     ans = input("Choose a " + str(A) + ". Select 1 for " + str(V[0]) + ', 2 for ' + str(V[1]) + ', 3 for ' + str(V[2]) + ".")
#     if ans == '1':
#         Y.unify(str(V[0]))
#     elif ans == '2':
#         Y.unify(str(V[1]))
#     elif ans == '3':
#         Y.unify(str(V[2]))
#     else:
#         Y.unify('Choose a number from 1 to 3!')
#     return True
#
# def read_py_menu2(A,V,Y):
#     Y.unify(input("Choose a " + str(A) + " from [" + str(V[0]) + ', ' + str(V[1]) + "]?"))
#     return True
#
# write_py.arity = 1
# read_py.arity = 3
#
# read_py_menu8.arity = 3
# read_py_menu3.arity = 3
# read_py_menu2.arity = 3
#
# registerForeign(write_py)
# registerForeign(read_py)
# # registerForeign(read_py_menu8)
# # registerForeign(read_py_menu3)
# # registerForeign(read_py_menu2)
#
# prolog.consult("KB.pl") # open the KB
# call(retractall(known))
# resultcount = 0
# for soln in prolog.query("recommendation(X).", maxresult=1):
#     resultcount = resultcount + 1
#     print("You should eat at " + soln['X'] + "!")
#
# if not resultcount:
#     print("No restaurant could be identified!")
