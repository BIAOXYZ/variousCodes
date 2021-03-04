import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # 同样参见LC300，这里对应的是`000300_algo2_impl_newlib.py`。

        if not envelopes:
            return 0

        envelopes.sort(key = lambda x : (x[0], -x[1]))
        heightList = [envelope[1] for envelope in envelopes]
        length = len(envelopes)

        longestList = []
        for i in range(length):
            if not longestList or heightList[i] > longestList[-1]:
                longestList.append(heightList[i])
            else:
                index = bisect.bisect_left(longestList, heightList[i])
                longestList[index] = heightList[i]
        return len(longestList)
        
"""
https://leetcode-cn.com/submissions/detail/151193833/

84 / 84 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 14.7 MB

执行用时：48 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了100.00%的用户
"""
"""
本想说几分钟后又通过调库产生了一个新的双百。但是仔细一看发现其实LeetCode平台有时延应该：
上一个的时间和空间分别是 68 ms，14.6 MB。这个时间确实更快，但是空间其实不如上一个啊。
所以应该就是和之前一个数据比的，刚才几分钟前提交的还没更新过去。。。
"""
