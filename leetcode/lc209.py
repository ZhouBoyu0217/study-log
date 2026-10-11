def solution(target:int,nums:list):
    n=len(nums)
    min_length=n+1
    total=0
    left=0
    for right in range(n):
        total+=nums[right]
        while total>=target:
            cur_length = right - left + 1
            if min_length > cur_length:
                min_length = cur_length
            total-=nums[left]
            left+=1
    if min_length!=n+1:
        print(min_length)
    else:
        print(0)

