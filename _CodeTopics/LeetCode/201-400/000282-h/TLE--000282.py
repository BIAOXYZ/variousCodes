class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        length = len(num)
        if length == 1:
            return [] if int(num) != target else [num]
        
        # "oprt" means "operator" 
        numOfOprt = length - 1
        res = []

        def backtrack(currOprtPos, currFormula):
            if currOprtPos == numOfOprt:
                if eval(currFormula) == target:
                    res.append(currFormula)
                return
            for op in ['+', '-', '*']:
                if num[currOprtPos + 1] == '0':
                    backtrack(currOprtPos + 1, currFormula + op + num[currOprtPos + 1])
                else:
                    for incr in range(1, numOfOprt - currOprtPos + 1):
                        backtrack(currOprtPos + incr, currFormula + op + num[currOprtPos + 1 : currOprtPos + incr + 1])

        if num[0] == '0':
            backtrack(0, num[0])
        else:
            for i in range(numOfOprt):
                backtrack(i, num[:i+1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/229520908/

13 / 23 个通过测试用例
状态：超出时间限制

最后执行的输入：
"2147483647"
2147483647
"""
