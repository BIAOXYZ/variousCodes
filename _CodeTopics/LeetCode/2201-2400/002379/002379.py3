class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)
        res = float('inf')
        for i in range(n-k+1):
            subBlock = blocks[i:i+k]
            diff = Counter(subBlock)['W']
            res = min(res, diff)
        return res
        
"""
https://leetcode.cn/submissions/detail/410883326/

执行用时：
60 ms
, 在所有 Python3 提交中击败了
6.01%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
43.72%
的用户
通过测试用例：
122 / 122
"""
