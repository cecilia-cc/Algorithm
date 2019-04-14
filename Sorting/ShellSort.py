def ShellSort(nums):
    """
    Advanced insertion sort 递减增量排序
    按照步长 每次插入排序

    Time complexity: worst/O(n(logn)^2);  avg/O(n(logn)^2);  best/O(nlogn);
    Space complexity: O(1)
    Unstable

    :param nums: unsorted array
    :return: sorted array
    """
    n = len(nums)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            # 每个步长进行插入排序
            temp = nums[i]
            j = i
            while j >= gap and nums[j-gap] > temp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = temp
        gap = gap //2
    return nums

input = [6,1,8,3,2,3,4,10,5]
print("shell sort")
print(input)
print(ShellSort(input))