class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:

        needEnergy = 0
        if initialEnergy <= sum(energy):
            needEnergy = sum(energy) + 1 - initialEnergy
        
        needExperience = 0
        n = len(experience)
        curr = initialExperience
        for i in range(n):
            if curr > experience[i]:
                curr += experience[i]
            else:
                needExperience += experience[i] + 1 - curr
                # 前面那个错是这里逻辑没理好，服了。。。
                curr = (experience[i] + 1) + experience[i]
        
        return needEnergy + needExperience
        
"""
https://leetcode.cn/submissions/detail/412455469/

执行用时：
28 ms
, 在所有 Python3 提交中击败了
97.04%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
11.85%
的用户
通过测试用例：
111 / 111
"""
