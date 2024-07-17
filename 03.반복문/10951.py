import sys

input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break
    a, b = map(int, line.split())
    print(a + b)
