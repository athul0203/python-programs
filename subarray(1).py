arr=list(map(int,input().split()))
target=int(input("enter the sum"))
found=False
for i in range(len(arr)):
    current_sum=0
    for j in range(i,len(arr)):
        current_sum+=arr[j]
        if current_sum==target:
            print(arr[i:j+1])
            found=True
            break
        if found:
            break
if not found:
    print(-1)