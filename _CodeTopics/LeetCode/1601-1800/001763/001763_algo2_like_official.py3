class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        # 官方答案位运算版本：由于有“缓存”，是 O(n^2) 的复杂度。
        # 而我之前那个遍历方法，对每一个子串都要从头开始算，所以是 O(n^3) 的复杂度。
        
        n = len(s)
        resStrPos, resStrLen = 0, 0
        # 这里外层循环到 n-1 就好，因为从最后一位（第 n-1 位）出发的
        # 字串长度只有 1，肯定不可能合法。不过按答案那种写成 n 也无所谓。
        for i in range(n-1):
            # 这里的 BitMap 实际上用一个数字处理了，更方便高效。
            lowerBitMap, upperBitMap = 0, 0
            for j in range(i, n):
                if s[j].islower():
                    # 这个是这个算法的精髓所在了。
                    lowerBitMap |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upperBitMap |= 1 << (ord(s[j]) - ord('A'))
                if lowerBitMap == upperBitMap and j - i + 1 > resStrLen:
                    resStrPos = i
                    resStrLen = j - i + 1
        return s[resStrPos : resStrPos + resStrLen]
        
"""
https://leetcode-cn.com/submissions/detail/264064292/

执行用时：52 ms, 在所有 Python3 提交中击败了57.69%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了95.67%的用户
通过测试用例：
73 / 73
"""
