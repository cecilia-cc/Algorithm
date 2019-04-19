class Solution:
    def findPeakElement(self, nums):
        # 套模板 LB1
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low


s = Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))