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
                    nextState[i] -= 1
                    nextState[3] = (nextState[3] + 1) % 2
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
https://leetcode-cn.com/submissions/detail/260688116/

33 / 106 个通过测试用例
状态：超出时间限制

最后执行的输入：
[2,33,90,62,43,21,96,20,18,84,74,61,100,5,11,4,67,96,18,6,68,82,32,76,33,93,33,71,32,30,63,37,46,95,51,63,77,63,84,52,78,66,76,66,9,73,92,79,65,29,42,64,46,84,95,71,15,68,55,9,22,64,56,83,52,47,38,19,59,32,89,29,56,84,57,90,96,19,38,13,49,65,93,8,30,15,12,40,84,7,6,75,36,31,6,78,64,33,49]
"""
"""
- 相比 `deliberate-WA--002029.py3`，这个肯定是“更接近正确答案的”，因为 `deliberate-WA--002029.py3` 里更新状态
  那部分的代码逻辑有个小错误，更新 round 时应该更新 nextState[3]，而不是更新 nextState[0]！
- 然而想吐槽的就是：“更错误的”代码反而跑过了 73 个用例，这个“更正确的代码”却只跑过了 33 个用例，第 34 个就超时跑不过了。
"""
