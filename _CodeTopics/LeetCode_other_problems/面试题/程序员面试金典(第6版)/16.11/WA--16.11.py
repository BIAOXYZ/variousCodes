class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """

        if k == 0:
            return []

        first = shorter * k
        res = [first]
        for i in range(k):
            res.append(res[-1] + longer - shorter)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/85701243/

59 / 60 个通过测试用例
状态：解答错误

输入：1
      1
      100000
输出：[100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000...
预期：[100000]
"""
