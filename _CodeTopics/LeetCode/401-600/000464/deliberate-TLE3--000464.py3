class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        # 这次用了字符串表示 currState，还是不行。。。坑死。
        # 于是故意提交一个，权当记录了。

        if sum(range(1, maxChoosableInteger+1)) < desiredTotal:
            return False
        
        memoDic = {}
        def memorize_search(currState, currSum, round):
            key = (currState, currSum, round)
            if key in memoDic:
                return memoDic[key]
            n = len(currState)
            for i in range(n-1, -1, -1):
                if currState[i] == '1':
                    if currSum + i >= desiredTotal:
                        memoDic[key] = round
                        return memoDic[key]
                    else:
                        break
            res = []
            for i in range(1, n):
                if currState[i] == '0':
                    continue
                else:
                    nextState = currState[:i] + '0' + currState[i+1:]
                    nextSum = currSum + i
                    res.append(memorize_search(nextState, nextSum, round^1))
            if all([res[i] == round^1 for i in range(len(res))]):
                memoDic[key] = round^1
            else:
                memoDic[key] = round
            return memoDic[key]
        
        state = '0' + '1' * maxChoosableInteger
        res = memorize_search(state, 0, 0)
        return True if res == 0 else False
        
"""
https://leetcode.cn/submissions/detail/316473065/

42 / 57 个通过测试用例
状态：超出时间限制

最后执行的输入：
20
209
"""
