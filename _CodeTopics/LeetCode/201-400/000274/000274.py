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
        return len(citations)
        
"""
https://leetcode-cn.com/submissions/detail/194362255/

81 / 81 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 13.3 MB

执行用时：4 ms, 在所有 Python 提交中击败了99.42%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了19.65%的用户
"""
