class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # 滑动窗口应该也可以吧，不过先试试排序。--> 但是总体看还是O(n^2)的复杂度，感觉又会超时。。。

        length = len(nums)
        newNums = [[nums[i], i] for i in range(length)]
        newNums.sort(key = lambda x : (x[0], x[1]))

        for i in range(length-1):
            # 忘了这个优化点了。。。
            if i > 0 and newNums[i][0] == newNums[i-1][0]:
                continue
            for j in range(i+1, length):
                if newNums[j][0] - newNums[i][0] > t:
                    break
                if abs(newNums[j][1] - newNums[i][1]) <= k:
                    return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/168917326/

53 / 54 个通过测试用例
状态：解答错误

输入：
[1,2,1,1]
1
0
输出：
false
预期：
true
"""
"""
这个反而是正确答案提交后，想到了一个优化点，就随手加了两行又去提交一次，结果竟然错了。
所以那个优化点是不对的，因为相同的值的index可能不同，有可能靠前那个index太小不符合，但是后面那个符合。傻了傻了。
"""
