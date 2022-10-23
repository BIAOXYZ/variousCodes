class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        # dp[i] 表示在前 i 份兼职工作中做选择，能达到的最大收益是多少。
        ## 那么就有，dp[0] = 0，因为第 0 份工作啥也没有，就是辅助的；
        ## 且最终的结果是 dp[n]，也就是（前） n 份兼职工作中做选择，能达到的最大收益。
        # 我们首先按工作结束时间排序。然后对于 dp[i]，其等于 max(dp[i-1], dp[k] + profit[i])。
        ## 也就是 dp[i] 分为不包含 profit[i] 和包含 profit[i] 两种情况，在这两种中取最大值。
        ## 不包含 profit[i] 的情况很好理解，包含 profit[i] 的情况则需要找到最晚的某个工作 k，
        ## 使得 k 和 第 i 个工作在时间上没有冲突。而显然不能线性查找这个 k，只能用二分。

        n = len(startTime)
        dp = [0 for _ in range(n+1)]
        # 为了在 for 循环中计算下一个 dp[i]，开始时间，结束时间和盈利都是不可缺少的，所以
        ## 下面这个临时变量里这三个数组的元素都要。
        tmp = sorted(zip(startTime, endTime, profit), key = lambda x : x[1])
        # 还需要搞一个只包含结束时间的数组，二分查找的时候用。此外，光知道这个数组还不行，还得维护一个数组和索引的对应关系。
        tmp2 = [tmp[i][1] for i in range(n)]
        ddic = defaultdict(list)
        for i, (_, etime, _) in enumerate(tmp):
            ddic[etime].append(i+1)
        # print(tmp, tmp2, ddic)
        for i in range(1, n+1):
            stime, _, prft = tmp[i-1]
            ind = bisect.bisect_right(tmp2, stime)
            if ind > 0:
                lastPossibleEndtime = tmp2[ind-1]
                # 万一不只一个这样的工作，取在 tmp 里排的最靠后的那个。
                k = ddic[lastPossibleEndtime][-1]
                dp[i] = max(dp[i-1], dp[k] + prft)
            else:
                dp[i] = max(dp[i-1], prft)
        return dp[n]
        
"""
https://leetcode.cn/submissions/detail/375850964/

执行用时：
192 ms
, 在所有 Python3 提交中击败了
72.86%
的用户
内存消耗：
38 MB
, 在所有 Python3 提交中击败了
5.87%
的用户
通过测试用例：
30 / 30
"""
