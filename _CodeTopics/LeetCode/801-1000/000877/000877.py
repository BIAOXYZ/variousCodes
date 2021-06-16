class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # 用归纳法推导可知，先选的人总能完全选到所有奇数index的石子堆或所有偶数index的石子堆，
        # 又因为这两种石子堆的数目肯定不可能相同，所以先选的必胜。。。
        return True
        
"""
https://leetcode-cn.com/submissions/detail/187300270/

46 / 46 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 12.9 MB

执行用时：8 ms, 在所有 Python 提交中击败了98.02%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了74.26%的用户
"""
