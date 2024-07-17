s = input()

_list = [-1]*26

for idx, char in enumerate(s):
    pos = ord(char)-ord('a')
    if _list[pos]==-1:
        _list[pos]=idx

for i in _list:
    print(i, end=' ')