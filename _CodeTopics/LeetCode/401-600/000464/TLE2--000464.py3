class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if sum(range(1, maxChoosableInteger+1)) < desiredTotal:
            return False
        
        memoDic = {}
        def memorize_search(currState, currSum, round):
            key = (tuple(currState), currSum, round)
            if key in memoDic:
                return memoDic[key]
            n = len(currState)
            for i in range(n-1, -1, -1):
                if currState[i] == 1:
                    if currSum + i >= desiredTotal:
                        memoDic[key] = round
                        return memoDic[key]
                    else:
                        break
            res = []
            for i in range(1, n):
                if currState[i] == 0:
                    continue
                else:
                    currState[i] = 0
                    currSum += i
                    res.append(memorize_search(currState, currSum, round^1))
                    currSum -= i
                    currState[i] = 1
            if all([res[i] == round^1 for i in range(len(res))]):
                memoDic[key] = round^1
            else:
                memoDic[key] = round
            return memoDic[key]
        
        state = [0] + [1] * maxChoosableInteger
        res = memorize_search(state, 0, 0)
        return True if res == 0 else False
        
"""
https://leetcode.cn/submissions/detail/316472804/

41 / 57 个通过测试用例
状态：超出时间限制

最后执行的输入：
20
210
"""
"""
坑爹玩意，这个就不该超时的，难道必须用数字表示 currState？就离谱。。。
"""
