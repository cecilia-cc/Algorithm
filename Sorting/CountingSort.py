
def CountingSort(nums):
    """
    (1) 找出待排序的数组中最大和最小的元素
    (2) 统计数组中每个值为i的元素出现的次数，存入数组C 的第 i项
    (3) 对所有的计数累加（从 C 中的第一个元素开始，每一项和前一项相加）
    (4) 反向填充目标数组：将每个元素i放在新数组的第C[i]项，每放一个元素就将C[i]减去1

    Time complexity: worst/avg/best/ O(n+k)
    Space complexity: O(k)
    Stable

    :param nums: unsorted array
    :return: sorted array
    """

    min = 2**31 -1
    max = 0
    for num in nums:
        if num < min: min = num
        if num > max: max = num
    count = [0]*(max-min+1)
    for i in nums:
        count[i-min] += 1
    index = 0
    # 反向放回
    for a in range(max-min+1):
        for c in range(count[a]):
            nums[index] = a+min
            index += 1
    return nums


# input = [1, 4, 2, 3, -1, 0, 25, -34, 8, 9, 1, 0]
input = [6,4,8,5,4,8,9]
print("counting sort")
print(input)
print(CountingSort(input))