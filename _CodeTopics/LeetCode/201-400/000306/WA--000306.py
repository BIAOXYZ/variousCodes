class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        length = len(num)
        res = [False]

        def backtrack(pos, currArr):
            if pos == length:
                res[0] = True
                return
            if num[pos] == '0':
                return
            for nextPos in range(pos+1, length+1):
                if len(currArr) < 3:
                    currArr.append(num[pos:nextPos])
                    backtrack(nextPos, currArr)
                    currArr.pop()
                else:
                    if num[pos:nextPos] == currArr[-1] + currArr[-2]:
                        currArr.append(num[pos:nextPos])
                        backtrack(nextPos, currArr)
                        currArr.pop()
        
        backtrack(0, [])
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/256775100/

25 / 42 个通过测试用例
状态：解答错误

输入：
"1"
输出：
true
预期结果：
false
"""
