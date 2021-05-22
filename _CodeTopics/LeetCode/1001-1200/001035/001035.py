class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        # 结果竟然是动态规划。。。这题有点脑筋急转弯的意思：从看起来是个几何题，变成了最长公共子序列：
        # LC1143 最长公共子序列 https://leetcode-cn.com/problems/longest-common-subsequence/
        # 不过我其实还没做过这道题，以前只做过 
        # LC300 最长递增子序列 https://leetcode-cn.com/problems/longest-increasing-subsequence/
        
        len1, len2 = len(nums1), len(nums2)
        dp = [[0 for i in range(len2)] for j in range(len1)]

        res = 0
        for i in range(len1):
            for j in range(len2):
                if i == j == 0:
                    if nums1[0] == nums2[0]: dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = max(dp[i][j-1], int(nums2[j] == nums1[0]))
                elif j == 0:
                    dp[i][j] = max(dp[i-1][j], int(nums1[i] == nums2[0]))
                else:
                    rowMax = dp[i][j-1]
                    colMax = dp[i-1][j]
                    for k in range(i):
                        newNum = nums2[j]
                        if dp[k][j-1] == dp[i][j-1] and nums1[k+1] == newNum:
                            rowMax += 1
                            break
                    for k in range(j):
                        newNum = nums1[i]
                        if dp[i-1][k] == dp[i-1][j] and nums2[k+1] == newNum:
                            colMax += 1
                            break
                    dp[i][j] = max(rowMax, colMax)
                res = max(res, dp[i][j])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/179958657/

74 / 74 个通过测试用例
状态：通过
执行用时: 8832 ms
内存消耗: 13.5 MB

执行用时：8832 ms, 在所有 Python 提交中击败了5.50%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了7.65%的用户
"""
