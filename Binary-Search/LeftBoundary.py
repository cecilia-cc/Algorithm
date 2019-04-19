def LeftBoundary1(nums,target):
    # 存在多个值，返回第一个下标
    # -> 数组有序，但包含重复元素
    # -> 数组部分有序，且不包含重复元素
    # e.g. LC 153
    low = 0
    high = len(nums)-1
    while low < high:
        mid = low + (high - low)//2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    if nums[low] == target:
        return low
    else: return -1

def LeftBoundary2(nums,target):
    # -> 数组部分有序，且包含重复元素
    # e.g. LC 154
    low = 0
    high = len(nums)-1
    while low < high:
        mid = low + (high - low)//2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid
        else:
            high -= 1
    if nums[low] == target:
        return low
    else: return -1

input = [1,3,3,3,3,4,4,6,14,65]
print("find left boundary")
print(LeftBoundary1(input,1))
print(LeftBoundary1(input,3))
print(LeftBoundary1(input,4))
