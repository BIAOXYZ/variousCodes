class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        # 第 232 场周赛第二题
        # 当时还写复杂了。。。
        # https://leetcode-cn.com/submissions/detail/154897747/ 

        for node in edges[0]:
            if node in edges[1]:
                return node
        
"""
https://leetcode-cn.com/submissions/detail/269713556/

执行用时：64 ms, 在所有 Python3 提交中击败了91.67%的用户
内存消耗：33.4 MB, 在所有 Python3 提交中击败了30.45%的用户
通过测试用例：
60 / 60
"""
