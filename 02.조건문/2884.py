h,m = map(int,input().split())

total_minute = h*60+m-45

h = total_minute//60
m = total_minute%60

if h<0:
	h=23

print(h, m) 