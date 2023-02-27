class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        dic1 = {item[0]:item[1] for item in items1}
        dic2 = {item[0]:item[1] for item in items2}
        res = []
        for value in range(1, 1001):
            if value not in dic1 and value not in dic2:
                continue
            res.append([value, dic1.get(value, 0) + dic2.get(value, 0)])
        return res
        
"""
https://leetcode.cn/submissions/detail/407037460/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
70.52%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
5.22%
的用户
通过测试用例：
49 / 49
"""
