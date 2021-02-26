class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # 滑动窗口 + 一个对应滑动窗口的字典，一起统计当前窗口内字母的频率 + 全局还剩下的频率 是否能满足k。

        freq = collections.Counter(s)
        left = right = 0
        maxLen = 0

        currFreq = {}
        while right < len(s):
            currFreq[s[right]] = currFreq.setdefault(s[right], 0)
            if freq[s[right]] >= k - currFreq[s[right]]:
                freq[s[right]] -= 1
                currFreq[s[right]] += 1
                right += 1
            else:
                maxLen = max(maxLen, right - left)
                currFreq = {}
                right += 1
                left = right
        maxLen = max(maxLen, right - left)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/149066191/

18 / 31 个通过测试用例
状态：解答错误

输入：
"ababacb"
3
输出：
5
预期：
0
"""
