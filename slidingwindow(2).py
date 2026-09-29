arr=list(map(int,input().split()))
k=int(input("enter the size"))
window_slide=sum(arr[:k])
min_slide=window_slide
for i in range(k,len(arr)):
    window_slide+=arr[i]
    window_slide-=arr[i-k]
    min_slide=min(window_slide,min_slide)
print(min_slide)