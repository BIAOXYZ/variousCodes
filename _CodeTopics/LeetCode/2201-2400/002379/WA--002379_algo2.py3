class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)
        res = float('inf')
        firstBlock = blocks[:k]
        ctr = Counter(firstBlock)
        for i in range(1, n-k+1):
            old, new = i-1, i+k-1
            ctr[blocks[old]] -= 1
            ctr[blocks[new]] += 1
            whiteStrNum = ctr['W']
            res = min(res, whiteStrNum)
        return res
        
"""
https://leetcode.cn/submissions/detail/410884795/

111 / 122 个通过测试用例
状态：解答错误

输入：
"BWWWBB"
6
输出：
null
预期结果：
3
"""
