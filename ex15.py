n =input("n= ")
sum = 0
for i in range (0,n):
	if i % 2 == 0:
		sum = sum - i
	else: sum = sum + i
print (sum)
