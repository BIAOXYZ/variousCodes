class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        # 这个看官方答案评论下面看到的，瞅了一眼没想通，回头再看下。
        return list(str(int(''.join(map(str, A)))+K))
        
"""
https://leetcode-cn.com/submissions/detail/140212186/

156 / 156 个通过测试用例
状态：通过
执行用时: 248 ms
内存消耗: 13.5 MB

执行用时：248 ms, 在所有 Python 提交中击败了92.13%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了69.11%的用户
"""
