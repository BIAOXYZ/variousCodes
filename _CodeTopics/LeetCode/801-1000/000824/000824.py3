class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        lis = sentence.split()
        res = []
        for i, word in enumerate(lis):
            if word[0] in 'aeiouAEIOU':
                currWord = word + 'ma' + 'a'*(i+1)
            else:
                currWord = word[1:] + word[0] + 'ma' + 'a'*(i+1)
            res.append(currWord)
        return ' '.join(res)
        
"""
https://leetcode-cn.com/submissions/detail/303168536/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
12.86%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
19.43%
的用户
通过测试用例：
99 / 99
"""
