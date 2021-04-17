class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        def cal_square_dis(x1, y1, x2, y2):
            return (x1 - x2)**2 + (y1 - y2)**2
        
        ans = []
        for query in queries:
            res = 0
            for point in points:
                if cal_square_dis(point[0], point[1], query[0], query[1]) <= query[2] * query[2]:
                    res += 1
            ans.append(res)
        return ans
    
"""
https://leetcode-cn.com/submissions/detail/169044057/

66 / 66 个通过测试用例
状态：通过
执行用时: 912 ms
内存消耗: 13.2 MB
"""
