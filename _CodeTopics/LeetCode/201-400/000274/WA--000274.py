class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                continue
            else:
                return i
        
"""
https://leetcode-cn.com/submissions/detail/194361936/

67 / 81 个通过测试用例
状态：解答错误

最后执行的输入：
[1]
输出：
null
预期结果：
1
"""
