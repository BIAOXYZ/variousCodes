class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stk = []
        for op in ops:
            if op not in "CD+":
                if len(op) == 1:
                    stk.append(int(op))
                else:
                    stk.append(-int(op[1]))
            elif op == 'C':
                stk.pop()
            elif op == 'D':
                stk.append(stk[-1]*2)
            elif op == '+':
                stk.append(stk[-1] + stk[-2])
        return sum(stk)
        
"""
https://leetcode-cn.com/submissions/detail/289515328/

5 / 39 个通过测试用例
状态：解答错误
输入：
["1","C","-62","-45","-68"]
输出：
-16
预期结果：
-175
"""
