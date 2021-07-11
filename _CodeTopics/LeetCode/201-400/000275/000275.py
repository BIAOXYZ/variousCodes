class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        length = len(citations)
        for i in range(-1, -length-1, -1):
            if citations[i] >= -i:
                continue
            else:
                return -i-1
        return length
        
"""
https://leetcode-cn.com/submissions/detail/194683530/

83 / 83 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 17.7 MB

执行用时：16 ms, 在所有 Python 提交中击败了96.67%的用户
内存消耗：17.7 MB, 在所有 Python 提交中击败了10.00%的用户
"""
