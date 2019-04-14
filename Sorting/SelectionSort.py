def SelectionSort(nums):
    """
    每次选择最小值 和左边的元素交换

    Time complexity: worst/avg/best  O(n^2)
    Space complexity: O(1)
    Unstable

    :param nums: unsorted array
    :return: sorted array
    """
    for i in range(len(nums)-1):
        min = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min]:
                min = j
        if i!=min:
            nums[i], nums[min] = nums[min], nums[i]
    return nums

input = [6,1,8,3,2,4,10,5]
print("select sort")
print(input)
print(SelectionSort(input))