class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)
        firstBlock = blocks[:k]
        ctr = Counter(firstBlock)
        res = ctr['W']
        for i in range(1, n-k+1):
            old, new = i-1, i+k-1
            ctr[blocks[old]] -= 1
            ctr[blocks[new]] += 1
            whiteStrNum = ctr['W']
            res = min(res, whiteStrNum)
        return res
        
"""
https://leetcode.cn/submissions/detail/410884978/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
90.76%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
78.80%
的用户
通过测试用例：
122 / 122
"""
