class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # 这个才是真正的滑动窗口实现，`000395.py`其实只是部分滑动窗口，但其核心还是递归。
        # 之所以不算正统的滑动窗口是因为缺少“两段性”：也就是只看频率没法（在不重新计算频率的情况下）确定
        # 若窗口 t 合法的时候， t+1或者t-1是不是一定合法。
        # https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/xiang-jie-mei-ju-shuang-zhi-zhen-jie-fa-50ri1/
        # 所以这里加上滑动窗口内字符种类数量这个指标，就可以了。

        maxLen = 0
        # debugstring = ''
        for kind in range(1, 27):
            left = right = 0
            currKind = 0
            currFreq = {}
            while right < len(s) and left <= right:
                tmpFreqRight = currFreq.get(s[right], 0)
                if tmpFreqRight == 0:
                    currKind += 1
                if currKind <= kind:
                    currFreq[s[right]] = currFreq.setdefault(s[right], 0) + 1
                    right += 1
                else:
                    if all([v >= k for v in currFreq.values()]):
                        maxLen = max(maxLen, right - left)
                        # if right - left == maxLen:
                        #     debugstring = s[left:right]
                        #     print left, right, debugstring, 1
                    currFreq[s[right]] = currFreq.setdefault(s[right], 0) + 1
                    while currKind > kind:
                        currFreq[s[left]] -= 1
                        tmpFreqLeft = currFreq.get(s[left], 0)
                        if tmpFreqLeft == 0:
                            currKind -= 1
                            del currFreq[s[left]]
                        left += 1
                    right += 1
            if all([v >= k for v in currFreq.values()]):
                maxLen = max(maxLen, right - left)
                # if right - left == maxLen:
                #     debugstring = s[left:right]
                #     print left, right, debugstring, 2
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/149178578/

31 / 31 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 13.1 MB

执行用时：124 ms, 在所有 Python 提交中击败了5.50%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了79.05%的用户
"""
"""
这题的滑动窗口法实现有Hard的难度了。
"""
