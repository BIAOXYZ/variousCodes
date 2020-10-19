class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        思路：
        1) 使用栈，并且对于新到的右括号，一定得是“右括号索引 - 栈顶元素索引”，而不能
        是“右括号索引 - 弹出栈的左括号索引”，后者无法正确处理比如 "()()"。
        2) 同时考虑到任何字符串最前面加一个")"并不会影响结果，所以加上一个右括号，使得
        栈底肯定是右括号。否则还是以上面的 "()()" 为例：
            0：0的左括号进栈，
            1：0的左括号出栈，坐标1减去栈顶的坐标0再加1，当前最长变成2 //但是其实栈顶没有元素
            2：2的左括号进栈，
            3：2的左括号出栈，坐标3减去栈顶的坐标0再加1，当前最长变成4 //但是其实栈顶没有元素
        3) 但是如果我们对这个串做处理，变成 s = ')' + s，那么s第一个元素是右括号就没法处理（除非做特殊处理）。
        所以答案栈里开始填个-1看来也是有一定的道理的。
        """

        if not s:
            return 0
        length = len(s)
        if length == 1:
            return 0

        maxlen = 0
        stack = []
        stack.append(-1)
        for i in range(length):
            ##print "i is %d, curren s[i] is %s" % (i, s[i])
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack != []:
                    currlen = i - stack[-1]
                    maxlen = max(maxlen, currlen)
                else:
                    stack.append(i)
            ##print stack
        return maxlen
        
"""
https://leetcode-cn.com/submissions/detail/86396622/

230 / 230 个通过测试用例
状态：通过
执行用时：28 ms
内存消耗：13.2 MB
"""
"""
# 看来用栈还是比动态规划快。

执行用时：28 ms, 在所有 Python 提交中击败了99.32%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了16.67%的用户
"""
