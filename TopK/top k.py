
import heapq
class Solution:
    def topklargerst(self, nums,k):
        # 最小堆
        # Time Complexity: O(n*logk)
        # 建堆 O(k) 调整堆 O(logk)
        # part1: klogk 建立堆并调整
        # part2: (n-k)logk 遍历（n-k)与堆顶比较 
        # klogk + (n-k)logk = O(n*logk)

        h=[]
        for i in range(k):
            heapq.heappush(h,nums[i])
        for i in range(k,len(nums)):
            if nums[i] > h[0]:
                heapq.heapreplace(h,nums[i])
        return h

    def topksmallest(self, nums,k):
        # 最大堆
        h=[]
        for i in range(k):
            heapq.heappush(h,-nums[i])
        for i in range(k,len(nums)):
            if nums[i] < -h[0]:
                heapq.heapreplace(h,-nums[i])
        return list(map(lambda x: -x,h))




s = Solution()
print(s.topklargerst([4,-1,5,7,1, 7,9,-5,-32,4],3))
print(s.topksmallest([4,-1,-2,5,7,1, 7,-7,9,-5,-32,4],3))