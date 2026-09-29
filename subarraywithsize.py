arr=list(map(int,input().split()))
k=int(input("enter the size"))
for i in range(len(arr)-k+1):
    subarray=arr[i:i+k]
    print(subarray)