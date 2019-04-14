def InsertionSort(nums):
    """
    left | right
    第一个元素不动 每次选中右边第一个元素插入左边
    左边shift找到插入的位置

    Time complexity: worst/O(n^2) ; avg/O(n^2) ; best/O(n) ;
    Space complexity: O(1)
    Stable

    :param nums: unsorted array
    :return: sorted array
    """
    for i in range(1,len(nums)):
        temp = nums[i]
        j = i
        while j>0 and nums[j-1]>=temp:
            nums[j] = nums[j-1]
            j -= 1
        if i != j:
            nums[j] = temp
    return nums

input = [6,1,8,3,2,4,10,5]
print("insertion sort")
print(input)
print(InsertionSort(input))