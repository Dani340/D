n =input("n= ")
sum = 1
for i in range (1,n):
	if i % 2 == 0:
		sum = sum * 2 * i
	else: sum= sum * i
print (sum)
