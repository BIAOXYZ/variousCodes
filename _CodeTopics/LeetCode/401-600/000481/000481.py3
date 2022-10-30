class Solution:
    def magicalString(self, n: int) -> int:
        
        s = "1221121"
        lis = list(s)
        # 1--1, 2--22, 2--11, 1--2, 1--1
        lastFreqInd, lastChInd = 4, 6 
        while n > len(lis):
            lastCh = lis[lastChInd]
            currCh = '2' if lastCh == '1' else '1'
            freq = int(lis[lastFreqInd+1])
            for i in range(freq):
                lis.append(currCh)
            lastFreqInd += 1
            lastChInd += freq
        return lis[:n].count('1')
        
"""
https://leetcode.cn/submissions/detail/377934428/

执行用时：
176 ms
, 在所有 Python3 提交中击败了
30.23%
的用户
内存消耗：
16.6 MB
, 在所有 Python3 提交中击败了
12.79%
的用户
通过测试用例：
64 / 64
"""
