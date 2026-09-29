arr=list(map(int,input().split()))
k=int(input())
window_slide=sum(arr[:k])
largest=window_slide/k
smallest=window_slide/k
for i in range(k,len(arr)):
    window_slide+=arr[i]
    window_slide-=arr[i-k]
    largest1=window_slide/k
    smallest1=window_slide/k
    largest=max(largest,largest1)
    smallest=min(smallest,smallest1)
print("largest",largest)
print("smallest",smallest)
