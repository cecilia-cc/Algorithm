
def QuickSort(nums):
    """
    Divide and conquer
    pivot-partion-recursive sort
    选择pivot；每个partition 小于pivot放左边 大于pivot放右边； 左边右边排序

    Time complexity: worst/O(n^2) ; avg/O(nlogn);  best/O(nlogn)
    Space complexity: O(logn)-O(n)
    Unstable

    :param nums: unsorted array
    :return: sorted array
    """

    # 递归法
    if len(nums) <= 1:
        return nums
    less = []
    greater = []
    pivot = nums.pop()  #last one -> pivot
    for num in nums:
        if num < pivot: less.append(num)
        else: greater.append(num)
    nums.append(pivot)
    return QuickSort(less) + [pivot] + QuickSort(greater)

##############################

def QuickSortInplace(nums):
    return q_sort(nums, 0, len(nums) - 1)

def q_sort(nums, left, right):
    if left < right:
        pivot = Partition(nums, left, right)

        q_sort(nums, left, pivot - 1)
        q_sort(nums, pivot + 1, right)
    return nums

def Partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]

    nums[left] = pivot
    return left

input = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
#input = [1, 4, 2, 3.6, 0, 25, 8, 9, 1, 0]
print("quick sort")
print(input)
print(QuickSort(input))
print(QuickSortInplace(input))