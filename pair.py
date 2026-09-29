arr=list(map(int,input().split()))
target=int(input("enter the sum"))
left=0
right=len(arr)-1
while left<right:
    current_sum=arr[left]+arr[right]
    if current_sum==target:
        print(arr[left],arr[right])
    left+=1
    right-=1
        
        