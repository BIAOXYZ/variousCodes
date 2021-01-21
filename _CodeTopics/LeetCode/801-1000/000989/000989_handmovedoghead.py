class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        # 好久没有碰到手动狗头题了。
        # 下一版写为啥这个转换可以。。。
        return [int(elem) for elem in list(str( int(''.join([str(elem) for elem in A])) + K ))]
        
"""
https://leetcode-cn.com/submissions/detail/140211023/

156 / 156 个通过测试用例
状态：通过
执行用时: 296 ms
内存消耗: 13.7 MB

执行用时：296 ms, 在所有 Python 提交中击败了65.35%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了43.90%的用户
"""
