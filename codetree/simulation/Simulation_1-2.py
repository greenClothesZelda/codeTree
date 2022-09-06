arr = list(map(int, input().split()))

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cal_day(m, d):
    sum=0
    for i in range(m):
        sum+=num_of_days[i]
    sum+=d
    return sum


print(cal_day(arr[2], arr[3]) - cal_day(arr[0], arr[1])+1)