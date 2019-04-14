
def MergeSort(nums):
    """
    Divide and conquer
    将有序的子序列合并，得到完全有序序列。

    Time complexity: worst/avg/best/ O(nlogn)
    Space complexity: O(n)
    Stable

    :param nums: unsorted array
    :return: sorted array
    """

    # 递归法
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    return merge(left, right)

def merge(left, right):
    ans = []
    while left and right:
        if left[0] <= right[0]:
            ans.append(left.pop(0))
        else:
            ans.append(right.pop(0))
    if left: ans += left
    if right: ans += right
    return ans

input = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
print("merge sort")
print(input)
print(MergeSort(input))