def RightBoundary(nums,target):
    # 存在多个值，返回第一个下标
    low = 0
    high = len(nums)-1
    while low < high:
        mid = low + (high - low)//2 + 1  # 注意这里 +1
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid
    if nums[high] == target:
        return high
    else: return -1

input = [1,3,3,3,3,4,4,6,14,65]
print("find right boundary")
print(RightBoundary(input,1))
print(RightBoundary(input,3))
print(RightBoundary(input,4))