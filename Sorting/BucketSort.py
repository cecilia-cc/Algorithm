
def BucketSort(nums):
    """
    把数组a划分为n个大小相同子区间（桶），每个子区间各自排序，最后合并。
    桶排序要求数据的分布必须均匀，不然可能会失效。
    计数排序是桶排序的一种特殊情况，可以把计数排序当成每个桶里只有一个元素的情况。

    Time complexity: worst/O(n^2); avg/O(n+k);  best/O(n+k)
    Space complexity: O(n+k)
    Stable

    :param nums: unsorted array
    :return: sorted array
    """
    buckets = [0] * (max(nums) - min(nums) +1)
    for i in range(len(nums)):
        buckets[nums[i]-min(nums)] += 1
    b = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            b += [i+min(nums)] * buckets[i]
    return b


input = [1, 4, 2, 3, -1, 0, 25, -34, 8, 9, 1, 0]
#input = [6,4,8,5,4,8,9]
print("bucket sort")
print(input)
print(BucketSort(input))