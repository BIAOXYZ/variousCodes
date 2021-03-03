class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # 先按第一个数排序，然后按第二个。感觉就是个排序后贪心啊，没明白是Hard原因。。。硬要说就是二维数组排序复杂度比较高？

        if not envelopes:
            return 0

        envelopes.sort(key = lambda x : (x[0], x[1]))
        res = 1
        currWidth, currHeight = envelopes[0][0], envelopes[0][1]
        for i in range(1, len(envelopes)):
            if envelopes[i][0] > currWidth and envelopes[i][1] > currHeight:
                res += 1
                currWidth = envelopes[i][0]
                currHeight = envelopes[i][1]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/150795199/

33 / 85 个通过测试用例
状态：解答错误

输入：
[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
输出：
4
预期：
5
"""
