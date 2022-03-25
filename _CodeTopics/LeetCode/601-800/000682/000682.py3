class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stk = []
        for op in ops:
            if op not in "CD+":
                if op[0].isdigit():
                    stk.append(int(op))
                else:
                    stk.append(-int(op[1:]))
            elif op == 'C':
                stk.pop()
            elif op == 'D':
                stk.append(stk[-1]*2)
            elif op == '+':
                stk.append(stk[-1] + stk[-2])
        return sum(stk)
        
"""
https://leetcode-cn.com/submissions/detail/289515584/

执行用时：40 ms, 在所有 Python3 提交中击败了42.79%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了67.16%的用户
通过测试用例：
39 / 39
"""
