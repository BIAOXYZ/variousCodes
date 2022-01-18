class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # 滑动窗口实现
        se = set(nums[:k+1])
        if len(se) < k + 1:
            return True
        
        for i in range(k+1, len(nums)):
            se.remove(nums[i-k-1])
            if nums[i] in se:
                return True
            se.add(nums[i])
        return False
        
"""
https://leetcode-cn.com/submissions/detail/260012841/

46 / 51 个通过测试用例
状态：解答错误

输入：
[1]
1
输出：
true
预期结果：
false
"""
