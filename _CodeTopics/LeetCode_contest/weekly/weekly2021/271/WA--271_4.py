import bisect
class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        
        n = len(fruits)
        positions = [fruit[0] for fruit in fruits]
        maxPos = positions[n-1]
        posfruit = {fruit[0]:fruit[1] for fruit in fruits}
        
        dic = {}
        def backtrack(pos, steps):
            key = (pos, steps)
            if key in dic:
                return dic[key]
            currval = 0 
            if pos in posfruit:
                currval += posfruit[pos]
                del posfruit[pos]
            ind = bisect.bisect(positions, pos)
            lind = ind - 1
            while lind > 0 and positions[lind] not in posfruit:
                lind -= 1
            rind = ind
            while rind < n and positions[rind] not in posfruit:
                rind += 1
            
            left = right = 0
            if lind > 0 and steps >= pos - positions[lind]:
                left = backtrack(positions[lind], steps - pos + positions[lind])
            if rind < n and steps >= positions[rind] - pos:
                right = backtrack(positions[rind], steps - positions[rind] + pos)
            dic[key] = currval + max(left, right)
            return dic[key]
        
        return backtrack(startPos, k)
    
"""
https://leetcode-cn.com/submissions/detail/247671253/

69 / 194 个通过测试用例
状态：解答错误

输入：
[[0,10000]]
200000
200000
输出：
0
预期：
10000
"""
