class Solution:
    def searchRange(self, nums, target):
        # 查找左右边界 套模板 LB RB
        ans = [-1,-1]
        if not nums or len(nums) == 0:
            return ans

        # find LB
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) //2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if nums[low] == target: ans[0] = low
        else: ans[0] = -1

        # find RB
        if ans[0] == -1 : return ans

        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2 + 1
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid
        if nums[high] == target:
            ans[1] = high
        else:
            ans[1] = -1
        return ans


s = Solution()
print(s.searchRange([5,7,7,8,8,10],8))
print(s.searchRange([5,7,7,8,8,10],9))
print(s.searchRange([1],1))
