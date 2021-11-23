from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        # {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
        # 如上所示，整体是上面的那个集合。但是要按字母的稀缺性（能够被排除出去的顺序）分批排除。
        
        # z, w, u, x, g
        batch1 = {'zero':'0', 'two':'2', 'four':'4', 'six':'6', 'eight':'8'}
        # h, f, s
        batch2 = {'three':'3', 'five':'5', 'seven':'7'}
        # o
        batch3 = {'one':'1', 'nine':'9'}

        freqDic = Counter(s)
        res = ''
        for batch in [batch1, batch2, batch3]:
            for num in batch.keys():
                minFreq = min(freqDic[ch] for ch in num)
                if minFreq > 0:
                    res += batch[num] * minFreq
                    for ch in num:
                        freqDic[ch] -= minFreq
        return ''.join(sorted(res))
        
"""
https://leetcode-cn.com/submissions/detail/241750881/

执行用时：72 ms, 在所有 Python 提交中击败了47.06%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了5.88%的用户
通过测试用例：
24 / 24
"""
