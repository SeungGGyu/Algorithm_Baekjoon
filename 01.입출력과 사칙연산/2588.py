a = int(input())
b = int(input())

list_b= list(str(b))

int_b = [int(b) for b in list_b]


print(a*int_b[2])
print(a*int_b[1])
print(a*int_b[0])
print(a*b)