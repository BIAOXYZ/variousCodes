class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        length = len(num)
        if length < 3:
            return False
        res = [False]

        def backtrack(pos, currArr):
            if pos == length:
                if len(currArr) >= 3:
                    res[0] = True
                return
            if num[pos] == '0':
                return
            for nextPos in range(pos+1, length+1):
                if len(currArr) < 2:
                    currArr.append(num[pos:nextPos])
                    backtrack(nextPos, currArr)
                    currArr.pop()
                else:
                    if int(num[pos:nextPos]) == int(currArr[-1]) + int(currArr[-2]):
                        currArr.append(num[pos:nextPos])
                        backtrack(nextPos, currArr)
                        currArr.pop()
        
        backtrack(0, [])
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/256778996/

37 / 42 个通过测试用例
状态：解答错误

输入：
"101"
输出：
false
预期结果：
true
"""
