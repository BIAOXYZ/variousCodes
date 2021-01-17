class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        
        dic = {}
        for rectangle in rectangles:
            key = min(rectangle[0], rectangle[1])
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        maxKey = max(dic.keys())
        return dic[maxKey]
    
"""
https://leetcode-cn.com/submissions/detail/139008247/

68 / 68 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13.4 MB
"""
