class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        
        # 不用管石子的值到底是多少，只需要关心模三的余数是 0、1、2 即可。
        # 那么每一个状态其实就是当前模三余数为 0、1、2 的石子的数量。
        # 于是第一反应就是类似 `LC913 猫和老鼠`，当然要比那个简单多了。

        memoDic = {}
        def memorize_search(currState):
            if key := tuple(currState) in memoDic:
                return memoDic[key]
            # 根据我们构造的 currState，有如下关系：
            zeros, ones, twos = currState[0], currState[1], currState[2]
            currRound, currSum = currState[3], currState[4]
            # 能判断胜负的情况：
            if currSum == 0:
                return True if currRound == 0 else False
            if zeros == ones == twos == 0:
                return False
            # 中间的还得继续往下的情况（是谁的round就先假设谁开始的结果是“输”）：
            res = False if currRound == 0 else True
            for i in range(3):
                if currState[i] > 0:
                    nextState = currState[:]
                    nextState[0] = (nextState[0] + 1) % 2
                    nextState[i] -= 1
                    nextState[4] = (nextState[4] + i) % 3
                    tmpRes = memorize_search(nextState)
                    if res != tmpRes:
                        res = tmpRes
                        break
            memoDic[key] = res
            return memoDic[key]

        stones = list(map(lambda x : x % 3, stones))
        # 前三个是当前剩余石子的状态（0，1，2的数量），第四个是当前round，第五个是当前已移除石子价值和。
        initState = [stones.count(i) for i in range(3)] + [0, 3]
        return memorize_search(initState)
        
"""
https://leetcode-cn.com/submissions/detail/260397880/

73 / 106 个通过测试用例
状态：解答错误

输入：
[5,1,2,4,3]
输出：
true
预期结果：
false
"""
"""
想的好好的记忆化搜索，写了半天，但是一看输入范围凉了。。。然后有个用例 [5,1,2,4,3] 明显
是错的，但是破电脑单步不起来了，三点半多了，不管了。。。
"""
