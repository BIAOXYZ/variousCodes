import heapq
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """

        n = len(days)
        dayAppleHeap = []
        heapq.heapify(dayAppleHeap)
        res = 0

        for i in range(n):
            if apples[i] > 0:
                heapq.heappush(dayAppleHeap, [i+days[i]-1, apples[i]])
            curr = [0, 0]
            while dayAppleHeap and (curr[0] < i or curr[1] == 0):
                curr = heapq.heappop(dayAppleHeap)
            if curr[0] >= i and curr[1] > 0:
                curr[1] -= 1
                res += 1
                if curr[1] > 0:
                    heapq.heappush(dayAppleHeap, curr)
        j = n
        while dayAppleHeap:
            curr = [0, 0]
            while dayAppleHeap and (curr[0] < j or curr[1] == 0):
                curr = heapq.heappop(dayAppleHeap)
            if curr[0] >= j and curr[1] > 0:
                j += 1
                curr[1] -= 1
                res += 1
                if curr[1] > 0:
                    heapq.heappush(dayAppleHeap, curr)
        
        return res
        
```
https://leetcode-cn.com/submissions/detail/251522192/

执行用时：552 ms, 在所有 Python 提交中击败了25.00%的用户
内存消耗：17.5 MB, 在所有 Python 提交中击败了25.00%的用户
通过测试用例：
70 / 70
```
