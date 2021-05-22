class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        # 官方答案里的 dp[i][j] 表示的是： “nums1[0:i] 和 nums2[0:j] 所能形成的最长公共子序列的长度”。
        # 而我的前一个实现 `001035.py` 里 dp[i][j] 是指： “nums1从0开始取到了i，nums2从0开始取到了j，所能形成的最长公共子序列的长度”。
        
        len1, len2 = len(nums1), len(nums2)
        dp = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

        res = 0
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    # 官方答案这一块的几行代码用了 dp[i+1][j+1] = balabala， 这样做前面两重for循环不会在
                    # len1 和 len2 后面加一了。但是我还是觉得我这种更自然，好理解。
                    if nums1[i-1] == nums2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len1][len2]
        
"""
https://leetcode-cn.com/submissions/detail/179961121/

74 / 74 个通过测试用例
状态：通过
执行用时: 136 ms
内存消耗: 13.3 MB

执行用时：136 ms, 在所有 Python 提交中击败了51.99%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了42.51%的用户
"""
