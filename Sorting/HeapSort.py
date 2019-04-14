
def HeapSort(nums):
    """
    Heap 近似完全二叉树 子节点总是小于/大于父节点
    https://www.cnblogs.com/chengxiao/p/6129630.html

    Time complexity: worst/avg/best/ O(nlogn)
    Space complexity: O(1)
    Unstable

    :param nums: unsorted array
    :return: sorted array
    """
    def sift_down(start, end):
        root = start
        while True:
            child = 2*root + 1
            if child > end:
                break
            if child + 1 <= end and nums[child] < nums[child+1]:
                child += 1
            if nums[root] < nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range(len(nums)//2, -1 ,-1):
        sift_down(start, len(nums)-1)
    # 堆排序
    print(nums)
    for end in range(len(nums)-1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(0,end-1)
    return nums


# input = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
input = [6,4,8,5,9]
print("heap sort")
print(input)
print(HeapSort(input))