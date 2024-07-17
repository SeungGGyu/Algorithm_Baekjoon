result = []
for i in range(10):
	num = int(input())
	a = num % 42 
	result.append(a)

result = set(result)
print(len(result))