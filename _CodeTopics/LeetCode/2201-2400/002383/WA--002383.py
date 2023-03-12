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
                curr = experience[i] + 1
        
        return needEnergy + needExperience
        
"""
https://leetcode.cn/submissions/detail/412454564/

93 / 111 个通过测试用例
状态：解答错误

输入：
1
1
[1,1,1,1]
[1,1,1,50]
输出：
52
预期结果：
51
"""
