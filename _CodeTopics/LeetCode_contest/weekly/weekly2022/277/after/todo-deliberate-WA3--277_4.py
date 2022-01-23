class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """

        # 单步跟了下，这个版本在输入为 [[2,1,0,0,2],[2,2,1,0,2],[0,2,2,1,0],[2,0,0,2,0],[2,0,0,1,2]] 
        # 时怎么感觉不论第 0 个用户怎么选都不行呢？真是无语了，还很难跟。。。

        COND1, COND2, COND3 = 0, 1, 2
        n = len(statements)
        res = [0]
        
        def check_match_0(l1, l2):
            for i in range(len(l1)):
                if l1[i] != 2 and l2[i] != 2 and l1[i] != l2[i]:
                    return False
            return True
        
        def check_match_1(l1, l2):
            for i in range(len(l1)):
                if l1[i] != 2 and l2[i] != 2 and l1[i] != 1 - l2[i]:
                    return False
            return True    
        
        def backtrack(ind, currState):
            if ind == n:
                ## print currState
                res[0] = max(res[0], currState.count(1))
                return
            for cond in range(3):
                nextState = currState[:]
                if cond == COND1:
                    if nextState[ind] == 0:
                        continue
                    nextState[ind] = 1
                    if not check_match_0(nextState, statements[ind]):
                        continue
                    breakFlag = 0
                    for i in range(n):
                        if statements[ind][i] != 2:
                            if nextState[i] == 2:
                                nextState[i] = statements[ind][i]
                            elif nextState[i] != statements[ind][i]:
                                breakFlag = 1
                                break
                    if not breakFlag:
                        backtrack(ind+1, nextState)
                elif cond == COND2:
                    if nextState[ind] == 1:
                        continue
                    nextState[ind] = 0
                    if not check_match_0(nextState, statements[ind]):
                        continue
                    breakFlag = 0
                    for i in range(n):
                        if statements[ind][i] != 2:
                            if nextState[i] == 2:
                                nextState[i] = statements[ind][i]
                            elif nextState[i] != statements[ind][i]:
                                breakFlag = 1
                                break
                    if not breakFlag:
                        backtrack(ind+1, nextState)
                else:
                    if nextState[ind] == 1:
                        continue
                    nextState[ind] = 0
                    if not check_match_1(nextState, statements[ind]):
                        continue
                    breakFlag = 0
                    for i in range(n):
                        if statements[ind][i] != 2:
                            if nextState[i] == 2:
                                nextState[i] = 1 - statements[ind][i]
                            elif nextState[i] != 1 - statements[ind][i]:
                                breakFlag = 1
                                break
                    if not breakFlag:
                        backtrack(ind+1, nextState)
        
        backtrack(0, [2]*n)
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/261558403/

48 / 82 个通过测试用例
状态：解答错误

输入：
[[2,1,0,0,2],[2,2,1,0,2],[0,2,2,1,0],[2,0,0,2,0],[2,0,0,1,2]]
输出：
0
预期结果：
1
"""
