class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # 第 237 场周赛第一题
        # 手动狗头
        return all( chr(chDigit) in sentence for chDigit in range(ord('a'), ord('z')+1) )
        
"""
https://leetcode.cn/submissions/detail/388767332/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
50.00%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
27.39%
的用户
通过测试用例：
79 / 79
"""
