class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        lis = list(word)
        for i, ch in enumerate(lis):
            if not ch.isdigit():
                lis[i] = ' '
        newWord = ''.join(lis)
        newLis = newWord.split()
        return len(set(map(int, newLis)))
        
"""
https://leetcode.cn/submissions/detail/387267004/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
52.44%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
11.56%
的用户
通过测试用例：
85 / 85
"""
