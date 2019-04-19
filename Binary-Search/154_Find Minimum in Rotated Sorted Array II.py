class Solution:
    def findMin(self, nums):
        # 套模板 L2
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        return nums[low]

s = Solution()
print(s.findMin([2,2,2,0,1]))
