n = int(input())

nums = input() # 이부분에서 이거를 int로 받는게 아니라 문자열로 받으면 되구나...

new_nums = []
for i in nums:
	new_nums.append(int(i))
	
print(sum(new_nums))