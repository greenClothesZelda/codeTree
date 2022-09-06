def re(_str):
    return _str[::-1]
_str = input()
if _str == re(_str):
    print("Yes")
else:
    print("No")
