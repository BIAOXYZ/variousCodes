import heapq
class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        
        n = len(milestones)
        m = [-milestones[i] for i in range(n)]
        heapq.heapify(m)
        for i in range(n-1):
            largest = -heapq.heappop(m)
            largest2 = -heapq.heappop(m)
            heapq.heappush(m, -1 * (largest - largest2))
        if m[0] in [-1, 0]:
            return sum(milestones)
        else:
            return sum(milestones) - (-m[0]) + 1
        
"""
https://leetcode-cn.com/submissions/detail/201916496/

69 / 73 个通过测试用例
状态：解答错误

最后执行的输入：
[5,7,5,7,9,7]
我的答案
39
预期答案
40
"""
