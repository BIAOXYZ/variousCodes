class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        
        # 最优的方案就是把 pattern 第一个字母放在 text 最前面
        # 或者把 pattern 第二个字母放在 text 最后面
        
        ch1, ch2 = pattern[0], pattern[1]
        if ch1 == ch2:
            cnt = text.count(ch1) + 1
            return cnt * (cnt-1) / 2
        
        l1, l2 = [], []
        for i, ch in enumerate(text):
            if ch == ch1:
                l1.append(i)
            if ch == ch2:
                l2.append(i)
        if not l1 and not l2:
            return 0
        elif not l1:
            return len(l2)
        elif not l2:
            return len(l1)
        
        res = 0
        pos1 = pos2 = 0
        while pos1 < len(l1) and pos2 < len(l2):
            if l1[pos1] > l2[pos2]:
                pos2 += 1
            else:
                res += len(l2) - pos2
                pos1 += 1
        return res + max(len(l1), len(l2))
    
"""
https://leetcode-cn.com/submissions/detail/286047593/

172 / 172 个通过测试用例
状态：通过
执行用时: 204 ms
内存消耗: 17.2 MB
"""
