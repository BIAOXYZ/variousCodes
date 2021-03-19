"""
# 我还是没明白答案里 op_to_binary_fn[token](num1, num2) 这步是怎么算的。。。
# 不过这里用到 try...except...finally... 这在leetcode里算很少见了。
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)
            
        return stack[0]
        
"""
https://leetcode-cn.com/submissions/detail/157372369/

20 / 20 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 16.1 MB

执行用时：60 ms, 在所有 Python3 提交中击败了31.40%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了18.75%的用户
"""
