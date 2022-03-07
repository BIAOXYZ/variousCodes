import bisect
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        # 第 64 场双周赛第三题。
        # 不过当时连第二题都没过，所以这道题可能根本就没看。

        candleInds = [i for i, ch in enumerate(s) if ch == '|']
        candles = [candleInds[i+1]-candleInds[i]-1 for i in range(len(candleInds)-1)]
        prefixSum = [0]
        for i in range(len(candles)):
            prefixSum.append(candles[i] + prefixSum[-1])
        ## print(candleInds, candles, prefixSum)
        
        res = []
        for q in queries:
            leftIndSearch = bisect.bisect_left(candleInds, q[0])
            rightIndSearch = bisect.bisect_right(candleInds, q[1])
            ## print(leftIndSearch, rightIndSearch)
            if leftIndSearch == rightIndSearch:
                res.append(0)
            else:
                leftInd, rightInd = leftIndSearch, rightIndSearch - 1
                res.append(prefixSum[rightInd] - prefixSum[leftInd])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/279207110/

执行用时：308 ms, 在所有 Python3 提交中击败了74.23%的用户
内存消耗：40.6 MB, 在所有 Python3 提交中击败了65.64%的用户
通过测试用例：
35 / 35
"""
