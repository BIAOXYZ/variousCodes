class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
   
        length = len(nums)
        if k >= length:
            k = k % length
        
        if k == 0 or length == 1:
            return nums

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
# https://leetcode-cn.com/submissions/detail/73115410/

33 / 35 个通过测试用例
状态：解答错误
输入：
[1,2,3,4,5,6]
4
输出：
[5,2,1,4,1,6]
预期：
[3,4,5,6,1,2]
"""
