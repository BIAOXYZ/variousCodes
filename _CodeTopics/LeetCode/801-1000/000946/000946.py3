class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stk = []
        n = len(pushed)
        i = j = 0
        while j < n:
            while popped[j] not in stk:
                stk.append(pushed[i])
                i += 1
            if stk and stk[-1] == popped[j]:
                stk.pop()
                j += 1
            else:
                return False
        return True
        
"""
https://leetcode.cn/submissions/detail/357132128/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
11.31%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
91.66%
的用户
通过测试用例：
151 / 151
"""
