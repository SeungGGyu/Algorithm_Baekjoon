num_list = []

for i in range(9):
	num_list.append(int(input()))

max_num = num_list[0]
max_num_index = 1
for i in range(9):
	if num_list[i]>=max_num:
		max_num = num_list[i]
		max_num_index = i+1

print(max_num)
print(max_num_index)