class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dic = {order[i]:i for i in range(len(order))}
        n = len(words)
        for i in range(1, n):
            firstWord, secondWord = words[i-1], words[i]
            len1, len2 = len(firstWord), len(secondWord)
            flag = False
            for j in range(min(len1, len2)):
                if dic[firstWord[j]] > dic[secondWord[j]]:
                    return False
                elif dic[firstWord[j]] < dic[secondWord[j]]:
                    flag = True
                    break
            if not flag and len2 < len1:
                return False
        return True
        
"""
https://leetcode.cn/submissions/detail/314477363/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
91.86%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
55.39%
的用户
通过测试用例：
120 / 120
"""
