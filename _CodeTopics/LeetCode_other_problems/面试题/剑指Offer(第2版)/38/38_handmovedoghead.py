class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # 手动狗头题
        return list(set(''.join(tupl) for tupl in itertools.permutations(s)))
        
"""
https://leetcode-cn.com/submissions/detail/188630343/

52 / 52 个通过测试用例
状态：通过
执行用时: 80 ms
内存消耗: 16.2 MB

执行用时：80 ms, 在所有 Python 提交中击败了98.03%的用户
内存消耗：16.2 MB, 在所有 Python 提交中击败了96.05%的用户
"""
