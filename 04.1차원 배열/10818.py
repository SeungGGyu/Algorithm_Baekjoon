n = int(input())
numbers = list(map(int, input().split()))

# 초기값 설정
_max = numbers[0]
_min = numbers[0]

# 최대값과 최소값 찾기

for i in range(n):
	if numbers[i] >= _max:
		_max= numbers[i]
	if numbers[i] <= _min:
		_min = numbers[i]


print(_min, _max)