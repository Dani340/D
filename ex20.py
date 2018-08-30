n =input("n= ")
m =input("m= ")
o = 180 - (n + m)
print (o)
if n == 90 or m == 90 or o == 90 :
	print ("dreptunghic")
if n > 90 or m > 90 or o > 90:
	print ("obtuz")
if n < 90 and m < 90 and o < 90:
	print ("acutitunghic") 
