import bisect
from sortedcontainers import SortedSet
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # 滑动窗口 + 有序容器（这里用的是 SortedSet，有序集合）

        length = len(nums)
        sw = SortedSet([nums[0]])  

        for i in range(1, length):
            # 此时滑动窗口sw已经满了， 需要删除最左边的元素
            if i > k:
                sw.discard(nums[i-k-1])
            if nums[i] in sw:
                return True
            else:
                sw.add(nums[i])
            ind = bisect.bisect_left(sw, nums[i])
            diff = 0
            if ind == 0:
                diff = sw[ind+1] - sw[ind]
            elif ind == len(sw) - 1:
                diff = sw[ind] - sw[ind-1]
            else:
                diff = min(sw[ind+1] - sw[ind], sw[ind] - sw[ind-1])
            if diff <= t:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/169072755/

3 / 54 个通过测试用例
状态：执行出错

执行出错信息：
Line 15: IndexError: list index out of range
最后执行的输入：
[]
0
0
"""
