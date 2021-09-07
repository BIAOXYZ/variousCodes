import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """

        """
        算法思路如下：以输入 k = 2, w = 0, profits = [1,2,3], capital = [0,1,1] 为例
        首先做完zip操作后，会得到：[(0, 1), (1, 2), (1, 3)]，然后再排个序得到：[(0, 1), (1, 3), (1, 2)]
        于是 zipped 是这样一个列表：里面按需要的资产数目递增；对于需要资产数相同的，能带来更大收益的靠前。

        然后就是搞一个堆，每轮都把符合条件的tuple入堆，并且一旦 zipped 后面的不满足入堆条件了，就开始从堆顶取
        能给资产带来最大增益的；然后继续，直到达到 k 个或者当前资产连最小的要求都达不到了。
        """

        length = len(capital)
        zipped = zip(capital, profits)
        ##print zipped
        zipped.sort(key = lambda x : (x[0], -x[1]))
        ##print zipped
        hp = []
        heapq.heapify(hp)

        num = 0
        pos = 0
        while num < k:
            while pos < length and zipped[pos][0] <= w:
                # 这里要处理一下，让能获得最大 profit 的在堆顶，所以tuple得变形。
                # 但是再深入一想，其实不需要往堆里插入tuple了，直接插数就行。
                heapq.heappush(hp, -zipped[pos][1])
                pos += 1
            if hp:
                tmp = heapq.heappop(hp)
                w = w + (-tmp)
                num += 1
            else:
                break
        return w
        
"""
https://leetcode-cn.com/submissions/detail/216528197/

35 / 35 个通过测试用例
状态：通过
执行用时: 712 ms
内存消耗: 44.9 MB

执行用时：712 ms, 在所有 Python 提交中击败了50.00%的用户
内存消耗：44.9 MB, 在所有 Python 提交中击败了6.25%的用户
"""
