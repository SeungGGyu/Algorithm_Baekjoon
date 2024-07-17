yun_year = int(input())

if yun_year % 4 ==0 and yun_year % 100 !=0 or yun_year % 400 ==0:
	print(1)
else:
	print(0)