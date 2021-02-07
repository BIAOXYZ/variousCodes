class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        length = len(arr)
        len2 = length - 1
        tmplis = [arr[i+1] - arr[i] for i in range(len2)]
        print tmplis    
        maxLen = 1

        left = 0
        while left < len2 and tmplis[left] == 0:
            left += 1
        right = left + 1

        while right < len2:
            if tmplis[right] == 0:
                maxLen = max(maxLen, right - left + 1)
                left = right + 1
                while left < len2 and tmplis[left] == 0:
                    left += 1
                right = left + 1
            elif tmplis[right] * tmplis[right-1] < 0:
                right += 1
            else:
                maxLen = max(maxLen, right - left + 1)
                left = right
                while left < len2 and tmplis[left] == 0:
                    left += 1
                right = left + 1
        if right == len2:
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/144564503/

89 / 89 个通过测试用例
状态：通过
执行用时: 252 ms
内存消耗: 16.5 MB

执行用时：252 ms, 在所有 Python 提交中击败了21.95%的用户
内存消耗：16.5 MB, 在所有 Python 提交中击败了27.05%的用户
"""
