class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        # trivial的暴力算法估计肯定超时。。。

        tmp = []
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            tmp.append([distance, point])
        
        tmp.sort()
        res = []
        for i in range(K):
            res.append(tmp[i][1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/122008138/

83 / 83 个通过测试用例
状态：通过
执行用时: 584 ms
内存消耗: 18.6 MB

执行用时：584 ms, 在所有 Python 提交中击败了95.04%的用户
内存消耗：18.6 MB, 在所有 Python 提交中击败了32.38%的用户
"""
"""
补充注释：本来以为肯定超时的，结果不但没超时，还超了95%的用户。。。简直了- -
"""
