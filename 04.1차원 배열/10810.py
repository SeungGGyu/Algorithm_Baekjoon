n,m = map(int, input().split())

basket = [0]*n

for i in range(m):
	a,b,c = map(int, input().split())
	for idx in range(a-1,b): ## 이부분 실수... 
		basket[idx] = c


for y in basket:
	print(y, end=' ')

