class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        # 这里故意提交一下错误版本，加深记忆。。。
        """
        # 对于第三个用例 ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]  来说，我的程序计算过程是：

        9+3
        12*-11
        6/-132
        10*-1
        -10+17
        7+5

        # 但是题目里给的解释是这样的：
          ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22

        # 很容易看出来，就是 6/-132 这里不同导致的结果不同。即使用python的eval()去算，也应该是-1，但是答案偏偏是0。
        # 然后评论里有个哥们是这么回复的： https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/comments/27195
        - python的 b / a 会向下取整， 比如 -1 / 132 = -1。 题目要求是取整数部分，那么负数的时候，实际应该是向上取整， 解决方法： int(b / float(a))
        - python3 b / a 会转为小数计算，所以直接 int(b / a)， 不能 b // a
        """

        stk = []
        for tk in tokens:
            if not stk or tk not in ["+", "-", "*", "/"]:
                stk.append(tk)
            else:
                rightNum = stk.pop()
                leftNum = stk.pop()
                print leftNum + tk + rightNum
                stk.append(str(eval(leftNum + tk + rightNum)))
        return int(stk[0])
        
"""
https://leetcode-cn.com/submissions/detail/157363873/

14 / 20 个通过测试用例
状态：解答错误

输入：
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：
12
预期：
22
"""
