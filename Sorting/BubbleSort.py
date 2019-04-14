
def BubbleSort(nums):
    """
    比较相邻元素 left > right 交换

    Time complexity: worst/O(n^2) ; avg/O(n^2) ; best/O(n) ;
    Space complexity: O(1)
    Stable

    :param nums: unsorted array
    :return: sorted array
    """
    for i in range(len(nums)-1, 0 ,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
    return nums

input = [6,1,8,3,2,4,10]
print("Bubble sort")
print(input)
print(BubbleSort(input))