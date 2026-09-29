arr=list(map(int,input().split()))
target=int(input("enter the sum"))
max_len=0
ans=[]
for i in range(len(arr)):
    current_sum=0
    for j in range(i,len(arr)):
        current_sum+=arr[j]
        if current_sum==target:
            if j-i+1>max_len:
                max_len=j-i+1
                ans=arr[i:j+1]
print(ans)