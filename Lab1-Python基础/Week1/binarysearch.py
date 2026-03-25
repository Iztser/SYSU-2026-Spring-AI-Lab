def binarySearch(arr,target):
    l = 0
    r = len(arr) - 1
    while(l <= r):
        mid = (r - l) // 2 + l
        if(arr[mid] < target):
            l = mid + 1
        elif(arr[mid] > target):
            r = mid - 1
        else:
            return mid
    return -1

str = input("请输入一个升序数组，用空格分隔")
arr = [int(x) for x in str.split()]
target = int(input("请输入要查找的目标："))
res = binarySearch(arr,target)
print(res)