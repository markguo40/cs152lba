recommendation('Wing Wing') :- distance(far), type(korean), price(high).
recommendation('Indian Veg') :- distance(medium), type(indian), price(low).
recommendation('King of Falafel') :- distance(close), type(arabic), price(low).
recommendation('Master Superfish') :- veg_options(no), distance(medium), type(british), price(medium).
recommendation('Fryers Delight') :- veg_options(no), distance(close), type(british), price(medium).
recommendation('Pret A Manger') :- distance(close), type(french), price(high).
recommendation('Wedge') :- distance(close), type(italian), price(medium).
recommendation('Pizza Pilgrims') :- distance(close), type(italian), price(medium).
recommendation('Bento Bab') :- distance(close), type(korean), price(low).
recommendation('Itsu') :- distance(far), type(chinese), price(medium).
recommendation('Great') :- veg_options(no), distance(close), type(mediterranean), price(high).
recommendation('Coin Laundry') :- distance(close), price(medium).
recommendation('Leather Lane') :- distance(close), price(low).
