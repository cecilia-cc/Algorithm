class Solution:
    def findMin(self, nums):
        # 套模板 LB1
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
            #if nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

s = Solution()
print(s.findMin([3,4,5,1,2] ))
