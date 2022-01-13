import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        hp = []
        heapq.heapify(hp)
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                heapq.heappush(hp, [nums1[i] + nums2[j], nums1[i], nums2[j]])
        
        res = []
        while hp and k > 0:
            res.append(heapq.heappop(hp)[1:])
            k -= 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/258255168/

执行用时：1800 ms, 在所有 Python3 提交中击败了14.81%的用户
内存消耗：150 MB, 在所有 Python3 提交中击败了9.51%的用户
通过测试用例：
32 / 32
"""
