class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        # 官方答案，用lambda表达式两行搞定。也可算手动狗头题了- -
        points.sort(key = lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]
        
"""
https://leetcode-cn.com/submissions/detail/122008684/

83 / 83 个通过测试用例
状态：通过
执行用时: 560 ms
内存消耗: 18.5 MB

执行用时：560 ms, 在所有 Python 提交中击败了99.29%的用户
内存消耗：18.5 MB, 在所有 Python 提交中击败了33.10%的用户
"""
