class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        # 使用map函数的手动狗头题。。。
        return list(map(int, str(int(''.join(map(str, A))) + K)))
        
"""
https://leetcode-cn.com/submissions/detail/140211540/

156 / 156 个通过测试用例
状态：通过
执行用时: 288 ms
内存消耗: 13.3 MB

执行用时：288 ms, 在所有 Python 提交中击败了68.50%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了91.06%的用户
"""
