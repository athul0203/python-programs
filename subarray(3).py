arr=list(map(int,input().split()))
target=int(input("enter the sum"))
min_length=len(arr)+1
ans=[]
for i in range(len(arr)):
    current_sum=0
    for j in range(i,len(arr)):
        current_sum+=arr[j]
        if target==current_sum:
            if j-i+1<min_length:
                min_length=j-i+1
                ans=arr[i:j+1]
print(ans)
          