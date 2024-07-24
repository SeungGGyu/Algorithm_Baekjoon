a,b = map(str, input().split())

result1 = int(a[::-1])
result2 = int(b[::-1])

if result1>result2:
    print(result1)
else:
    print(result2)
    