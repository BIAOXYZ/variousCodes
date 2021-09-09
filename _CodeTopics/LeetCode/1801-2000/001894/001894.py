class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """

        remainder = k % sum(chalk)
        for i in range(len(chalk)):
            if remainder < chalk[i]:
                return i
            else:
                remainder -= chalk[i]
        
"""
https://leetcode-cn.com/submissions/detail/217362141/

72 / 72 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 21.1 MB

执行用时：44 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：21.1 MB, 在所有 Python 提交中击败了20.00%的用户
"""
