class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        # 这次用数字表示 currState，总行了吧。

        if sum(range(1, maxChoosableInteger+1)) < desiredTotal:
            return False
        
        memoDic = {}
        def memorize_search(currState, currSum, round):
            key = (currState, currSum, round)
            if key in memoDic:
                return memoDic[key]
            for i in range(maxChoosableInteger-1, -1, -1):
                if (currState >> i) == 1:
                    if currSum + i + 1 >= desiredTotal:
                        memoDic[key] = round
                        return memoDic[key]
                    else:
                        break
            # 除了 currState 的优化，下面的部分也有些优化：
            ## 不再搞一个 res 数组，然后每次必须把整个 for 循环都走完，最后再判断；
            ## 而是根据题意，只要有一个能返回 round 的结果，就立刻返回，后面的 for 循环不用再走了，类似“剪枝”的效果。
            # 所以所谓的“状态压缩”的核心其实就是“剪枝”！那么这个应该算是一个状态压缩动态规划（状压dp）的典型例子了。
            for i in range(maxChoosableInteger):
                if (currState >> i) & 1 == 0:
                    continue
                else:
                    nextState = currState - 2**i
                    nextSum = currSum + i + 1
                    if memorize_search(nextState, nextSum, round^1) == round:
                        memoDic[key] = round
                        return memoDic[key]
            memoDic[key] = round^1
            return memoDic[key]
        
        state = 2**maxChoosableInteger - 1
        res = memorize_search(state, 0, 0)
        return True if res == 0 else False
        
"""
https://leetcode.cn/submissions/detail/316630715/

执行用时：
4172 ms
, 在所有 Python3 提交中击败了
11.15%
的用户
内存消耗：
179.6 MB
, 在所有 Python3 提交中击败了
43.07%
的用户
通过测试用例：
57 / 57
"""
