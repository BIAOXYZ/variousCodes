class Solution:
    def solveEquation(self, equation: str) -> str:

        leftEquation, rightEquation = equation.split('=')
        ## print(leftEquation, rightEquation)

        def parse_and_calculate(s):
            # 多加一个 dummy 的加号/正号，从而不用再额外处理最后一个 cur 了。
            s += '+'
            numVariable = numFactor = 0
            if s[0] == '-':
                cur = '-'
                start = 1
            else:
                cur = ''
                start = 0
            for i in range(start, len(s)):
                ch = s[i]
                if ch not in '+-':
                    cur += ch
                else:
                    if cur[-1] == 'x':
                        if len(cur) == 1:
                            numVariable += 1
                        elif len(cur) == 2 and cur[0] == '-':
                            numVariable -= 1
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
https://leetcode.cn/submissions/detail/348558170/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
41.61%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
39.13%
的用户
通过测试用例：
59 / 59
"""
