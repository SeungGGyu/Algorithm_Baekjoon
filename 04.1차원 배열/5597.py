num_list = list(range(1,31))

for i in range(28):
	a = int(input())
	if a in num_list:
		num_list.remove(a)

print(min(num_list))
print(max(num_list))