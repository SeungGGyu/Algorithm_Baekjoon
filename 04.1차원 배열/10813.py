n, m = map(int, input().split())

num_list = []

for i in range(1,n+1):
	num_list.append(i)

for i in range(m):
	a,b = map(int, input().split())
	c = num_list[a-1]
	num_list[a-1] = num_list[b-1]
	num_list[b-1] = c

for i in num_list:
	print(i , end=' ')
