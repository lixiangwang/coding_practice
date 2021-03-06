"""
703. Kth Largest Element in a Stream
在流数据中找到K个最大的元素。

https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, 
which contains initial elements from the stream. For each call to the method KthLargest.add, 
return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
############################################################################################################
############################################################################################################
"""
思路：维护一个k的小顶堆
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)  # 堆化，小顶堆
        # 移除最小的元素，循环后，只保留k个最大的
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        # 列表比k小，则直接将元素加入堆中
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        # else if 待加入的元素比第一个元素大，那起码第一个元素会被淘汰出这个KthLargest
        elif val > self.pool[0]:
            # 用新值替换堆中最小的值
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Your KthLargest object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
val = 10
obj = KthLargest(k, nums)
param_1 = obj.add(val)
print(param_1)  # 7
