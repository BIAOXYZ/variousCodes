class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ctr = Counter(s)
        s = deque(list(s))
        t, p = [], []
        
        def get_curr_min_ch(dic):
            for ch in [chr(i) for i in range(ord('a'), ord('z')+1)]:
                if ch in dic and dic[ch] > 0:
                    return ch
        
        while s:
            currMinCh = get_curr_min_ch(ctr)
            while t and currMinCh >= t[-1]:
                p.append(t.pop())
            while s and s[0] != currMinCh:
                ch = s.popleft()
                t.append(ch)
                ctr[ch] -= 1
            ch = s.popleft()
            p.append(ch)
            ctr[ch] -= 1
        while t:
            p.append(t.pop())
        return ''.join(p)
    
"""
https://leetcode.cn/submissions/detail/371252765/

61 / 61 个通过测试用例
状态：通过
执行用时: 1176 ms
内存消耗: 17.5 MB
"""
"""
真TM郁闷死，相比 WA--314_3.py，就是一个大于号改成大于等于号，就这一点区别，身体状态差直接想不起来了。
而且这题根本就不需要搞双端队列，反正 s 只会往后面移动，只要改成用 i 从 0 到 len(s) 不断移动到末尾就行了。
"""
