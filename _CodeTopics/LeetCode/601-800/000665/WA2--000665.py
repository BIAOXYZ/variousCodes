class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        flag = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                flag += 1
                if flag > 1:
                    return False
                if i >= 1 and nums[i-1] > nums[i+1]:
                    return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/144278707/

323 / 335 个通过测试用例
状态：解答错误

输入：
[5,7,1,8]
输出：
false
预期：
true
"""
"""
注：乐了。。。这个题可以啊- -骚完第一次还有第二次。。。哈哈。
"""
