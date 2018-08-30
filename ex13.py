n =input("n= ")
sum = 1
while n > 0:
	if n % 2 == 0:
		sum = sum * (n % 10)
	print(n % 10)
	n /= 10
print (sum)

