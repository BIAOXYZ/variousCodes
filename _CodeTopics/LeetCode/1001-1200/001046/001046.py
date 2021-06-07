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
        return stones[0] if stones else 0
        
"""
https://leetcode-cn.com/submissions/detail/184915232/

70 / 70 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了76.27%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了10.17%的用户
"""
