class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # 先试试最trivial的每次取最大的前两个，减掉小的，如果有剩下的再放回去然后重新排序。看会不会超时。

        while len(stones) > 1:
            stones.sort()
            weight1 = stones.pop()
            weight2 = stones.pop()
            if weight1 - weight2 != 0:
                stones.append(weight1 - weight2)
        return stones[0]
        
"""
https://leetcode-cn.com/submissions/detail/184915185/

4 / 70 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    return stones[0]
Line 16 in lastStoneWeight (Solution.py)
    ret = Solution().lastStoneWeight(param_1)
Line 40 in _driver (Solution.py)
    _driver()
Line 50 in <module> (Solution.py)
最后执行的输入：
[2,2]
"""
