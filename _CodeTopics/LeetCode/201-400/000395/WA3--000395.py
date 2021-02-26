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
            # 字典的get()方法和setdefault()方法的一大区别就是：如果某个key不在，setdefault()会额外插入这个key。
            # 并设置对应的val为默认值，但是get()方法不会插入这个key。
            tmpFreq = currFreq.get(s[right], 0)
            if freq[s[right]] >= k - tmpFreq:
                freq[s[right]] -= 1
                currFreq[s[right]] = currFreq.setdefault(s[right], 0) + 1
                right += 1
            else:
                if all([v >= k for v in currFreq.values()]):
                    maxLen = max(maxLen, right - left)
                else:
                    maxLen = self.longestSubstring(s[left:right], k)
                currFreq = {}
                right += 1
                left = right
        maxLen = max(maxLen, right - left)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/149066636/

29 / 31 个通过测试用例
状态：解答错误

输入：
"bbaaacddcaabdbd"
3
输出：
0
预期：
3
"""
