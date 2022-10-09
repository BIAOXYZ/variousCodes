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
            while t and currMinCh > t[-1]:
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
https://leetcode.cn/submissions/detail/371172670/

54 / 61 个通过测试用例
状态：解答错误

输入：
"vzhofnpo"
输出：
"fnopohzv"
预期：
"fnohopzv"
"""
