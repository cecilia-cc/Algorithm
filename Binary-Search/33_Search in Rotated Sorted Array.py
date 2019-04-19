# LC 33
class Solution:
    def search(self, nums, target):
        i = 0
        j = len(nums) - 1
        flag = -1
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                flag = mid
                break
            if nums[mid] >= nums[i]:
                if nums[i] <= target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            if nums[mid] <= nums[j]:
                if nums[mid] < target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1
        return flag

s = Solution()
print(s.search([5,6,7,8,9,2,3,4],7))