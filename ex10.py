odd_numbers = 0
even_numbers = 1
for i in range (10,20):
	if i % 2 == 0:
		odd_numbers = odd_numbers + i
		
	else: even_numbers = even_numbers * i
print (even_numbers)
print (odd_numbers)
