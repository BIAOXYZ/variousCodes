class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        if not image:
            return []
        if not image[0]:
            return [[]]
        rows, cols = len(image), len(image[0])
        visited = []
        original_color = image[sr][sc]

        def is_legal_coordinate(sr, sc):
            if sr < 0 or sr > rows - 1: return False
            if sc < 0 or sc > cols - 1: return False
            return True

        def dfs(sr, sc):
            if not is_legal_coordinate(sr, sc) or image[sr][sc] != original_color:
                return
            image[sr][sc] = newColor
            for newcoor in [[sr-1,sc],[sr+1,sc],[sr,sc-1],[sr,sc+1]]:
                dfs(newcoor[0], newcoor[1])
            return
        
        dfs(sr,sc)
        return image
        
"""
https://leetcode-cn.com/submissions/detail/98744383/

16 / 277 个通过测试用例
状态：执行出错

执行出错信息：
Line 25: RuntimeError: maximum recursion depth exceeded
最后执行的输入：
[[0,0,0],[0,1,1]]
1
1
1
"""
