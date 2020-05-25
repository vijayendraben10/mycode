
# function that calls itself

#n! = (n)(n-1)(n-2)(n-3)...1
total = 1

def factorial(n):
	global total
	if n == 1:
		return 0
	else:
		total *= n
		return factorial(n-1)
factorial(60)
print(total)