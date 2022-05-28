class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        alphabeta = [chr(i) for i in range(ord('a'), ord('z')+1)]
        Alphabeta = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        def compare_name(n1, n2):
            len1, len2 = len(n1), len(n2)
            for i in range(min(len1, len2)):
                if n1[i] in Alphabeta and n2[i] in alphabeta:
                    return False
                elif n2[i] in Alphabeta and n1[i] in alphabeta:
                    return True
                elif n1[i] > n2[i]:
                    return True
                elif n2[i] > n1[i]:
                    return False
            return True if len1 > len2 else False
        
        ddic = defaultdict(int)
        n = len(senders)
        for i in range(n):
            s, m = senders[i], messages[i]
            ddic[s] += len(m.split())
        
        maxkey, maxval = '', 0
        for k, v in ddic.items():
            if v > maxval or (v == maxval and compare_name(k, maxkey)):
                maxkey, maxval = k, v
        return maxkey
    
"""
https://leetcode.cn/submissions/detail/319192851/

65 / 65 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 19.6 MB
"""
