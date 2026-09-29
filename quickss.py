def quick(arr):
    if len(arr)<=1:
        return arr
    left=[]
    right=[]
    pivot=arr[-1]
    for i in range(len(arr)-1):
        if pivot>arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick(left)+[pivot]+quick(right)
arr=list(map(int,input().split()))
print(quick(arr))