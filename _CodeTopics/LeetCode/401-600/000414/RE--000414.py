class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 手动狗头题
        return sorted(set(nums))[-3] if len(nums) >= 3 else sorted(set(nums))[-1]
        
"""
https://leetcode-cn.com/submissions/detail/226158565/

3 / 31 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    return sorted(set(nums))[-3] if len(nums) >= 3 else sorted(set(nums))[-1]
Line 9 in thirdMax (Solution.py)
    ret = Solution().thirdMax(param_1)
Line 31 in _driver (Solution.py)
    _driver()
Line 41 in <module> (Solution.py)
最后执行的输入：
[1,1,2]
"""
