n,m= map(int, input().split())

basket = []
for i in range(1,n+1):
	basket.append(i)


for _ in range(m):
	i,j = map(int, input().split())
	
	basket[i-1:j] = basket[i-1:j][::-1]

for i in basket:
	print(i, end= ' ' )
