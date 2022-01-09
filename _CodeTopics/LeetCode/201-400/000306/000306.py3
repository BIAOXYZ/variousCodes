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
                if len(currArr) < 2 or (len(currArr) >= 2 and currArr[-1] == currArr[-2] == '0'):
                    currArr.append('0')
                    backtrack(pos+1, currArr)
                    currArr.pop()
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
https://leetcode-cn.com/submissions/detail/256779375/

执行用时：40 ms, 在所有 Python3 提交中击败了20.13%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了16.11%的用户
通过测试用例：
42 / 42
"""
