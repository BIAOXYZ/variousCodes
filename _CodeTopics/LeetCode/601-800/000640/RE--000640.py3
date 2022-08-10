class Solution:
    def solveEquation(self, equation: str) -> str:

        leftEquation, rightEquation = equation.split('=')
        ## print(leftEquation, rightEquation)

        def parse_and_calculate(s):
            # 多加一个 dummy 的加号/正号，从而不用再额外处理最后一个 cur 了。
            s += '+'
            numVariable = numFactor = 0
            cur = ''
            for ch in s:
                if ch not in '+-':
                    cur += ch
                else:
                    if cur[-1] == 'x':
                        if len(cur) == 1:
                            numVariable += 1
                        else:
                            numVariable += int(cur[:-1])
                    else:
                        numFactor += int(cur)
                    cur = ch if ch == '-' else ''
            return numVariable, numFactor

        leftX, leftFactor = parse_and_calculate(leftEquation)
        rightX, rightFactor = parse_and_calculate(rightEquation)
        ## print(leftX, leftFactor, rightX, rightFactor)
        finalX, finalFactor = leftX - rightX, rightFactor - leftFactor
        if finalX == 0 and finalFactor != 0:
            return "No solution"
        elif finalX == 0 and finalFactor == 0:
            return "Infinite solutions"
        else:
            return "x=" + str(finalFactor // finalX)
        
"""
https://leetcode.cn/submissions/detail/348510776/

5 / 59 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: string index out of range
    if cur[-1] == 'x':
Line 16 in parse_and_calculate (Solution.py)
    leftX, leftFactor = parse_and_calculate(leftEquation)
Line 26 in solveEquation (Solution.py)
    ret = Solution().solveEquation(param_1)
Line 57 in _driver (Solution.py)
    _driver()
Line 68 in <module> (Solution.py)
最后执行的输入：
"-x=-1"
"""
