n =input("n= ")
par = 0
impar = 0
while n > 0:
	if n % 10 % 2 == 0:
		par = par + 1
	else: impar = impar + 1
	n /= 10
print (par)
print (impar)
