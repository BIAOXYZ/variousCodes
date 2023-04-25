class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # 手动狗头题
        return list( zip( *sorted(zip(heights, names), reverse=True) ) )[1]
        
"""
https://leetcode.cn/submissions/detail/427888332/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
55.68%
的用户
内存消耗：
15.5 MB
, 在所有 Python3 提交中击败了
12.99%
的用户
通过测试用例：
68 / 68
"""
