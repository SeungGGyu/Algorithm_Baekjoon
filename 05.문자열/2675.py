n = int(input())

for i in range(n):
	a,b = map(str, input().split())
	a = int(a)
	result = ''
	for char in b:
		result += char*a
	print(result)

	
	
	
	