class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # 对用例 [3,3,3,3,4] 还是有问题，但是打算先提交了。

        if sum(matchsticks) % 4 != 0:
            return False
        else:
            edgeLen = sum(matchsticks) // 4
        
        def working_on_which_edge(tup):
            for i in range(4):
                if sum(tup[i]) == edgeLen:
                    continue
                else:
                    return i
            return 3

        matchsticks.sort()
        memoDic = {}
        def backtrack(usedSticks, remainedSticks):
            if usedSticks in memoDic:
                return memoDic[usedSticks]
            if not remainedSticks:
                memoDic[usedSticks] = True
                return memoDic[usedSticks]
            currWokingEdgeInd = working_on_which_edge(usedSticks)
            # 如果已经到了第四条边了，说明前三个边长为 edgeLen 的边的组合已经找到了
            # 一共就四条边，剩下那条肯定也是合法的了。
            if currWokingEdgeInd == 3:
                memoDic[usedSticks] = True
                return memoDic[usedSticks]
            else:
                currSum = sum(usedSticks[currWokingEdgeInd])
                for i, stick in enumerate(remainedSticks):
                    if currSum + matchsticks[stick] <= edgeLen:
                        tmpTuple = usedSticks[currWokingEdgeInd] + (matchsticks[stick],)
                        nextUsedSticks = []
                        for j in range(4):
                            if j == currWokingEdgeInd:
                                nextUsedSticks.append(tmpTuple)
                            else:
                                nextUsedSticks.append(usedSticks[j])
                        nextUsedSticks = tuple(nextUsedSticks)
                        nextRemainedSticks = remainedSticks.remove(remainedSticks[i])
                        if backtrack(nextUsedSticks, nextRemainedSticks):
                            memoDic[usedSticks] = True
                            return memoDic[usedSticks]
                    else:
                        memoDic[usedSticks] = True
                        return memoDic[usedSticks]
        
        n = len(matchsticks)
        usedSticks = ((),(),(),())
        remainedSticks = list(range(n))
        return backtrack(usedSticks, remainedSticks)
        
"""
https://leetcode.cn/submissions/detail/320789420/

158 / 183 个通过测试用例
状态：解答错误

输入：
[3,3,3,3,4]
输出：
true
预期结果：
false
"""
