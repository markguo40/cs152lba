recommendation('Wing Wing') :- veg_options(yes), distance(far), type(korean), price(high).
recommendation('Indian Veg') :- veg_options(yes), distance(medium), type(indian), price(low).
recommendation('King of Falafel') :- veg_options(yes), distance(close), type(arabic), price(low).
recommendation('Master Superfish') :- veg_options(no), distance(medium), type(british), price(medium).
recommendation('Fryers Delight') :- veg_options(no), distance(close), type(british), price(medium).
recommendation('Pret A Manger') :- veg_options(yes), distance(close), type(french), price(high).
recommendation('Pizza Pilgrims') :- veg_options(yes), distance(close), type(italian), price(medium).
recommendation('Bento Bab') :- veg_options(yes), distance(close), type(korean), price(low).
recommendation('Itsu') :- veg_options(yes), distance(far), type(chinese), price(medium).
recommendation('Great') :- veg_options(no), distance(close), type(mediterranean), price(high).
recommendation('Wedge') :- veg_options(yes), distance(close), type(italian), price(medium).
recommendation('Coin Laundry') :- veg_options(yes), distance(close), price(medium).
recommendation('Leather Lane') :- veg_options(yes), distance(close), price(low).

veg_options(X) :- ask(veg_options, X).
type(X):- menuask8(type, X, [korean, indian, arabic, british, french, chinese, mediterranean, italian]).
distance(X):- menuask3(distance, X, [close, medium, far]).
price(X):- menuask3(price, X, [low, medium, high]).

multivalued(none).

% Asking clauses

ask(A, V):-
known(yes, A, V), % succeed if true
!. % stop looking

ask(A, V):-
known(_, A, V), % fail if false
!, fail.

ask(A, V):-
\+ multivalued(A),
known(yes, A, V2),
V \== V2,
!, fail.

ask(A, V):-
read_py(A,V,Y), % get the answer
asserta(known(Y, A, V)), % remember it
Y == yes. % succeed or fail

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

menuask8(A, V, MenuList):-
known(yes, A, V), % succeed if true
!. % stop looking

menuask8(A, V, MenuList):-
\+ multivalued(A),
known(yes, A, V2),
V \== V2,
!, fail.

menuask8(A, V, MenuList) :-
read_py_menu8(A,MenuList,Y),
check_val8(Y, A, V, MenuList),
asserta( known(yes, A, Y) ),
Y == V.

menuask3(A, V, MenuList):-
known(yes, A, V), % succeed if true
!. % stop looking

menuask3(A, V, MenuList):-
\+ multivalued(A),
known(yes, A, V2),
V \== V2,
!, fail.

menuask3(A, V, MenuList) :-
read_py_menu3(A,MenuList,Y),
check_val3(Y, A, V, MenuList),
asserta( known(yes, A, Y) ),
Y == V.

check_val8(Y, A, V, MenuList) :-
member(Y, MenuList), !.

check_val8(Y, A, V, MenuList) :-
write_py(Y), write_py('Try again.'), nl,
menuask8(A, V, MenuList).

check_val3(Y, A, V, MenuList) :-
member(Y, MenuList), !.

check_val3(Y, A, V, MenuList) :-
write_py(Y), write_py('Try again.'), nl,
menuask3(A, V, MenuList).
