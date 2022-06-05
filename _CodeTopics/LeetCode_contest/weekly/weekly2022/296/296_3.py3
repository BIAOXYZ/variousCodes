class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        n = len(nums)
        dic = {nums[i]:i for i in range(n)}
        m = len(operations)
        for i in range(m):
            before, after = operations[i]
            ind = dic[before]
            del dic[before]
            dic[after] = ind
        
        for num, ind in dic.items():
            nums[ind] = num
        return nums
    
"""
https://leetcode.cn/submissions/detail/321759277/

80 / 80 个通过测试用例
状态：通过
执行用时: 176 ms
内存消耗: 62.3 MB
"""
