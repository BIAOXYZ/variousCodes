class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        # 主要思想就是分段处理：把初始时有方向的骨牌的 index 先统计一下，然后根据区间分别处理即可。
        # 但是这个实现起来确实不好写的感觉，再加上晚了不想优化了，所以代码挺丑的。

        n = len(dominoes)
        if n < 2:
            return dominoes
        
        initStateInds = []
        for i, card in enumerate(dominoes):
            if card != '.':
                initStateInds.append(i)
        if not initStateInds:
            return dominoes
        
        res = list(dominoes)
        def deal_with_left(firstInd):
            if firstInd == 0 or dominoes[firstInd] == 'R':
                return
            for i in range(firstInd):
                res[i] = 'L'
        def deal_with_right(lastInd):
            if lastInd == n-1 or dominoes[lastInd] == 'L':
                return
            for i in range(lastInd+1, n):
                res[i] = 'R'
        def deal_with_middle(leftInd, rightInd):
            leftState, rightState = dominoes[leftInd], dominoes[rightInd]
            if leftState == rightState:
                for i in range(leftInd+1, rightInd):
                    res[i] = leftState
            elif leftState == 'L' and rightState == 'R':
                return
            elif leftState == 'R' and rightState == 'L':
                midInd = leftInd + (rightInd - leftInd) // 2
                # 此时中间有奇数个点，最中间那个保持不变，其他分别按左右边来变化。
                if (rightInd - leftInd) % 2 == 0:
                    for i in range(leftInd+1, midInd):
                        res[i] = leftState
                    for i in range(midInd+1, rightInd):
                        res[i] = rightState
                else:
                    for i in range(leftInd+1, midInd+1):
                        res[i] = leftState
                    for i in range(midInd+1, rightInd):
                        res[i] = rightState

        deal_with_left(initStateInds[0])
        deal_with_right(initStateInds[-1])
        length = len(initStateInds)
        if length > 1:
            for i in range(length-1):
                deal_with_middle(initStateInds[i], initStateInds[i+1])
        return ''.join(res)
        
"""
https://leetcode-cn.com/submissions/detail/270974374/

执行用时：248 ms, 在所有 Python3 提交中击败了50.81%的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了33.06%的用户
通过测试用例：
43 / 43
"""
