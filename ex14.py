n =input("n= ")
copie = n
m = 0
while n > 0:
	m = m * 10 + n % 10
	n = n / 10
print (n)
print (m)
if copie > m: 
	print("primul e mai mare")
elif m > copie:
	print("al doilea e mai mare")
else: print("sunt egale")
