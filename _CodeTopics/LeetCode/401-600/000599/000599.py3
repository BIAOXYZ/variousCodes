class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        dic1 = {restaurant:i for i, restaurant in enumerate(list1)}
        dic2 = {restaurant:i for i, restaurant in enumerate(list2)}
        dic = {}
        for restaurant in dic1:
            if restaurant in dic2:
                dic[restaurant] = dic1[restaurant] + dic2[restaurant]
        minVal = min(dic.values())
        res = [k for k, v in dic.items() if v == minVal]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/282668929/

执行用时：52 ms, 在所有 Python3 提交中击败了78.50%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了19.23%的用户
通过测试用例：
136 / 136
"""
