def BaiscBinarySearch(nums,target):
    # 不减序列 nums
    # 存在多个值，返回任意一个下标
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

input = [1,3,3,3,3,4,4,6,14,65]
print("Basic Binary Search")
print(BaiscBinarySearch(input,4))
