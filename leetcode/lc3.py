s=input()
arr=[-1]*128
right=0
left=0
max_length=0
for right in range(0,len(s)):

    idx=ord(s[right])
    if arr[idx]>=left:#只有left在当前窗口
        left=arr[idx]+1
    arr[idx]=right
    cur_length=right-left+1
    if cur_length>max_length:
        max_length=cur_length
print(max_length)
