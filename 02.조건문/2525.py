h,m = map(int , input().split())

do_m = int(input())

m += do_m

if m>=60:
	h += m // 60 
	m = m % 60 
	

if h>=24:
	h = h % 24 
	

print(h, m)