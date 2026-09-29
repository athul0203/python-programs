arr=list(map(int,input().split()))
k=int(input("enter the size"))
window_slide=sum(arr[:k])
max_slide=window_slide
for i in range(k,len(arr)):
    window_slide+=arr[i]
    window_slide-=arr[i-k]
    max_slide=max(window_slide,max_slide)
print(max_slide)