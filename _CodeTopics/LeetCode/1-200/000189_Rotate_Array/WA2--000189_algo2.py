class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if k == 0:
            return nums
        
        length = len(nums)
        if k >= length:
            k = k % length

        if length % k != 0:
            curr = nums[0]
            indnext = k
            for i in range(length):
                temp = nums[indnext]
                nums[indnext] = curr
                curr = temp
                if indnext + k >= length:
                    indnext = (indnext + k) % length
                else:
                    indnext = indnext + k
        else:
            sublen = length / k
            for j in range(k):
                curr = nums[j]
                indnext = j + k
                for i in range(sublen):
                    temp = nums[indnext]
                    nums[indnext] = curr
                    curr = temp
                    if indnext + k >= length:
                        indnext = (indnext + k) % length
                    else:
                        indnext = indnext + k
        return nums

"""
# https://leetcode-cn.com/submissions/detail/73113746/

3 / 35 个通过测试用例
状态：执行出错
执行出错信息：
Line 16: ZeroDivisionError: integer division or modulo by zero
最后执行的输入：
[1]
1
"""
