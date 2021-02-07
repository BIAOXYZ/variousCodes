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
        while arr[left] == 0 and left < len2:
            left += 1
        right = left + 1

        while right < len2:
            if arr[right] == 0:
                maxLen = max(maxLen, right - left)
                left = right + 1
                while arr[left] == 0 and left < len2:
                    left += 1
                right = left + 1
            elif tmplis[right] * tmplis[right- 1] < 0:
                right += 1
            else:
                maxLen = max(maxLen, right - left)
                left = right
                while arr[left] == 0 and left < len2:
                    left += 1
                right = left + 1
        return maxLen + 1
        
"""
https://leetcode-cn.com/submissions/detail/144563223/

76 / 89 个通过测试用例
状态：解答错误

输入：
[0,1,1,0,1,0,1,1,0,0]
输出：
2
预期：
5
"""
