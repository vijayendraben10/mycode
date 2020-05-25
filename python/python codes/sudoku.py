array = [5, 3, 0, 0, 7, 0, 0, 0, 0]
array_s = []
numbers = []  

for i in range(1, 10, 1):
	numbers.append(i)


print(numbers)


for j in range(len(array)):
	if array[j] != 0:
		array_s.append(array[j])


print(array_s)


for h in array_s:
	numbers.remove(h)

print(numbers)

for i in range(len(array)):
	if array[i] == 0:
		array[i] = numbers[x]
		x += 1


print("FINAL ANSWER \n")
print(array)		