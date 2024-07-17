n,x = map(int, input().split())

numbers = list(map(int, input().split()))

s=[]
for i in range(n):
	if numbers[i]<x:
		s.append(numbers[i])

print(' '.join(map(str, s)))