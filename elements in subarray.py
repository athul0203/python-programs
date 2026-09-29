arr=list(map(int,input().split()))
current_sum=arr[0]
max_sum=arr[0]
temp=0
start=0
end=0
for i in range(1,len(arr)):
    if arr[i]>current_sum+arr[i]:
        current_sum=arr[i]
        temp=i
    else:
        current_sum+=arr[i]
    if current_sum>max_sum:
        max_sum=current_sum
        start=temp
        end=i
print(arr[start:end+1])
        