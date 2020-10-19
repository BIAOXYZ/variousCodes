class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        res = 0
        stack = []

        for i in range(length-1):
            stack.append(s[i])
            j = i + 1
            # 没有这个flag的原来的代码，对于输入 "001011"，会输出4，但正确结果是3。
            # 原因就是比如第一个0，后来出现1以后，再出现0就不能入栈了！
            diff_elem_appear = False
            while stack != [] and j < length:
                if s[j] == stack[-1]:
                    if not diff_elem_appear:
                        stack.append(s[j])
                    else:
                        break
                else:
                    stack.pop()
                    diff_elem_appear = True
                j += 1
            if stack == []:
                res += 1
            else:
                # 否则要把栈清空一下，不然可能会对下一个i的循环有影响。
                stack = []
        return res
        
"""
https://leetcode-cn.com/submissions/detail/96416160/

85 / 90 个通过测试用例
状态：超出时间限制
"""
