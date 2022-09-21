class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        usingLis = []
        for elem in arr:
            flag = False
            if usingLis:
                if elem != usingLis[0]:
                    return False
                else:
                    flag = True
                    usingLis.pop(0)
            else:
                for lis in pieces:
                    if lis and elem == lis[0]:
                        flag = True
                        lis.pop(0)
                        usingLis = lis
            if not flag:
                return False
        return True
        
"""
https://leetcode.cn/submissions/detail/365786716/

执行用时：
28 ms
, 在所有 Python3 提交中击败了
97.56%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
25.85%
的用户
通过测试用例：
84 / 84
"""
