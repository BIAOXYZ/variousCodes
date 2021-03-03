class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # 两个元素都按升序排序后贪心是不行的，看看这个用例就知道了：
        # [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
        # 最后结果长度只有4，对应这个：[[2,100],[3,200],[4,300],[5,400]]。
        # 但其实正确答案是5，对应这个：[[2,100],[3,200],[5,250],[6,360],[7,380]]。

        # 参考了答案里纯动态规划的算法：排序还是要排序的，但是针对第一个元素是递增排序，针对第二个元素是递减排序。
        # 这样的做的用处是在排序完成后，第一个维度就可以不用管了，直接在第二个维度求一个最长递增子序列长度即可。
        # 最长递增子序列就是LC300，一道经典题了。

        if not envelopes:
            return 0

        envelopes.sort(key = lambda x : (x[0], -x[1]))
        heightList = [envelope[1] for envelope in envelopes]
        length = len(envelopes)
        dp = [1 for _ in range(length)]

        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if heightList[j] > heightList[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/150799297/

85 / 85 个通过测试用例
状态：通过
执行用时: 5284 ms
内存消耗: 15.3 MB

执行用时：5284 ms, 在所有 Python 提交中击败了66.45%的用户
内存消耗：15.3 MB, 在所有 Python 提交中击败了67.10%的用户
"""
