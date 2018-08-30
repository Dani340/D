n =input("n= ")
par = 0
impar = 1
while n > 0:
	if n % 10 % 2 == 0:
		par = par + (n % 10)
	else: impar = impar * (n % 10)
	n /= 10
print (impar)
print (par)
