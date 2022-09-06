def method(arr):
    for elem in arr:
        if(elem % 2 == 0):
            print(elem//2, end = " ")
        else:
            print(elem, end = " ")
input()
arr = list(map(int, input().split()))
method(arr[:])