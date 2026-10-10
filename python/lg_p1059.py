arr=list(0 for i in range(1005))
n=int(input())
num=list(map(int,input().split()))
for a in num:
    arr[a]+=1
temp=list()
for i in range(1,1001):
    if arr[i]>0:
        temp.append(i)
print(f"{len(temp)}")
for a in temp:
    print(f"{a}",end=" ")
