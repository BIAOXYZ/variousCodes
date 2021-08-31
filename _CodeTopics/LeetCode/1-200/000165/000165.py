class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = version1.split('.')
        v2 = version2.split('.')
        len1, len2 = len(v1), len(v2)
        for i in range(max(len1, len2)):
            num1 = int(v1[i]) if i < len1 else 0
            num2 = int(v2[i]) if i < len2 else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0
        
"""
https://leetcode-cn.com/submissions/detail/213660246/

81 / 81 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.2 MB

执行用时：12 ms, 在所有 Python 提交中击败了94.72%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了21.55%的用户
"""
