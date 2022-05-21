class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if sum(range(1, maxChoosableInteger+1)) < desiredTotal:
            return False
        
        def backtrack(currState, currSum, round):
            n = len(currState)
            for i in range(n-1, -1, -1):
                if currState[i] == 1:
                    if currSum + i >= desiredTotal:
                        return round
                    else:
                        break
            res = []
            for i in range(1, n):
                if currState[i] == 0:
                    continue
                else:
                    currState[i] = 0
                    currSum += i
                    res.append(backtrack(currState, currSum, round^1))
                    currSum -= i
                    currState[i] = 1
            if all([res[i] == 1 for i in range(len(res))]):
                return 1
            return 0
        
        state = [0] + [1] * maxChoosableInteger
        res = backtrack(state, 0, 0)
        return True if res == 0 else False
        
"""
https://leetcode.cn/submissions/detail/316471570/

4 / 57 个通过测试用例
状态：解答错误

输入：
10
40
输出：
true
预期结果：
false
"""
