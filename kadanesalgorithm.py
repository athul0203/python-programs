arr=list(map(int,input().split()))
current_sum=arr[0]
max_sum=arr[0]
for i in range(1,len(arr)):
    current_sum=max(current_sum+arr[i],arr[i])
    max_sum=max(current_sum,max_sum)
print(max_sum)
    
        