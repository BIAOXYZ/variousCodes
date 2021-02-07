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
        # 我发现这种情况（遍历结束，但是最后的合法结果需要再算一次）在滑动窗口题里很常见。
        if maxLen != 0:  # 不然的话对于只有一个元素的arr，比如[100]，结果会是2。
            maxLen = max(maxLen, right - left)
        return maxLen + 1
        
"""
https://leetcode-cn.com/submissions/detail/144564349/

86 / 89 个通过测试用例
状态：解答错误

输入：
[4,5]
输出：
1
预期：
2
"""
