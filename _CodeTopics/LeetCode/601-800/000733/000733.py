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
            if not is_legal_coordinate(sr, sc) or image[sr][sc] != original_color or [sr, sc] in visited:
                return
            image[sr][sc] = newColor
            visited.append([sr, sc])
            for newcoor in [[sr-1,sc],[sr+1,sc],[sr,sc-1],[sr,sc+1]]:
                dfs(newcoor[0], newcoor[1])
            return
        
        dfs(sr,sc)
        return image
        
"""
https://leetcode-cn.com/submissions/detail/98746378/

277 / 277 个通过测试用例
状态：通过
执行用时：60 ms
内存消耗：13.2 MB
"""
"""
执行用时：60 ms, 在所有 Python 提交中击败了93.79%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了7.14%的用户
"""
