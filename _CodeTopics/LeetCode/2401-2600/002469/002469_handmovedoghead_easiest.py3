class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:

        # 甚至比手动狗头题还要手动狗头题。。。这个应该是 LeetCode 史上最简单题吧？
        return [celsius + 273.15, celsius * 1.80 + 32.00]
        
"""
https://leetcode.cn/submissions/detail/415866646/

执行用时：
52 ms
, 在所有 Python3 提交中击败了
5.69%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
54.37%
的用户
通过测试用例：
74 / 74
"""
