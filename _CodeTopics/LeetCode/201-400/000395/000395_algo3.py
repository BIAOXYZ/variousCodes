class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # 分治 + 递归

        freq = collections.Counter(s)
        maxLen = 0

        separators = set(filter(lambda x : freq[x] < k, freq.keys()))
        if not separators:
            return len(s)
        
        separatorIndexes = [-1]
        for i, ch in enumerate(s):
            if ch in separators:
                separatorIndexes.append(i)
        separatorIndexes.append(len(s))
        for i in range(len(separatorIndexes)-1):
            left = separatorIndexes[i] + 1
            right = separatorIndexes[i+1]
            # print left, right, s[left:right]
            maxLen = max(maxLen, self.longestSubstring(s[left:right], k))
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/149188282/

31 / 31 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 13.3 MB

执行用时：52 ms, 在所有 Python 提交中击败了20.18%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了47.62%的用户
"""
