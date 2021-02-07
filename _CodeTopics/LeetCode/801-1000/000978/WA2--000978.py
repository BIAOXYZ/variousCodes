class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        length = len(arr)
        len2 = length - 1
        tmplis = [arr[i+1] - arr[i] for i in range(len2)]
        ##print tmplis    
        maxLen = 0

        left = 0
        while left < len2 and tmplis[left] == 0:
            left += 1
        right = left + 1

        while right < len2:
            if tmplis[right] == 0:
                maxLen = max(maxLen, right - left)
                left = right + 1
                while left < len2 and tmplis[left] == 0:
                    left += 1
                right = left + 1
            elif tmplis[right] * tmplis[right-1] < 0:
                right += 1
            else:
                maxLen = max(maxLen, right - left)
                left = right
                while left < len2 and tmplis[left] == 0:
                    left += 1
                right = left + 1
        return maxLen + 1
        
"""
https://leetcode-cn.com/submissions/detail/144564076/

82 / 89 个通过测试用例
状态：解答错误

输入：
[0,8,45,88,48,68,28,55,17,24]
输出：
2
预期：
8
"""
