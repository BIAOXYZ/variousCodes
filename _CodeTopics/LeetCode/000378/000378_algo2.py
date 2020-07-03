class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        """
        上一个超时是因为比较急，用了每次两路归并，多次循环。这个肯定时间上不如一次多路归并。
        而且多路归并还可以选择在到达第k个元素时候就终止，重复多次二路归却必须完全排序好才行。
        """

        length = len(matrix)
        # 不同于官方答案初始化堆的时候把第一列推进去，这里把第一行推进去。因此后面也会
        # 相应的有些小改动：比如判断什么时候不推了，这个是看行是否到头，而不是看列是否到头。
        # 此外堆里的元素官方用了个tuple，应该效率更好点，但是直觉上肯定还是更习惯list，所以这里
        # 组成了一个list往堆里推。
        minhp = [[matrix[0][y], 0, y] for y in range(length)]
        heapq.heapify(minhp)

        for i in range(k-1):
            elem, x, y = heapq.heappop(minhp)
            if x != length - 1:
                heapq.heappush(minhp, [matrix[x+1][y], x+1, y])
        return heapq.heappop(minhp)[0]
        
"""
https://leetcode-cn.com/submissions/detail/84336767/

85 / 85 个通过测试用例
状态：通过
执行用时：228 ms
内存消耗：18.1 MB
"""
