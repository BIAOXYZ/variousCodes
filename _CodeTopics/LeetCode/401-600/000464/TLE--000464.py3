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
            # 这里正确的逻辑应该是：
            ## 如果所有的结果都是 round^1，那么肯定是对手获胜，返回 round^1；
            ## 只要有一个结果是 round，那么当前玩家一定会选这个路线，从而获胜，也就是返回 round。
            # 此外，怀疑可能会超时，需要用类似记忆化搜索的方式处理一下。
            if all([res[i] == round^1 for i in range(len(res))]):
                return round^1
            return round
        
        state = [0] + [1] * maxChoosableInteger
        res = backtrack(state, 0, 0)
        return True if res == 0 else False
        
"""
https://leetcode.cn/submissions/detail/316472207/

5 / 57 个通过测试用例
状态：超出时间限制

最后执行的输入：
18
79
"""
