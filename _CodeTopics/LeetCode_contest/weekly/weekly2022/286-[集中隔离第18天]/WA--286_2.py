class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # dic = {}
        # state = [False, -1, -1]
        # for i in range(len(nums)):
        #     if i == 0:
        #         continue
        #     ch = nums[i-1]
        #     if nums[i] == ch:
        #         if not state[0]:
        #             state = [True, i-1, 2]
        #         else:
        #             state[2] += 1
        #     else:
        #         if not state[0]:
        #             continue
        #         else:
        #             dic[state[1]] = state[2]
        #             state = [False, -1, -1]
        # if state[0]:
        #     dic[state[1]] = state[2]
        # print(dic)
        
        n = len(nums)
        if n < 2:
            return 0
        
        res = 0
        ptr1, ptr2 = 0, 1
        while ptr2 < n:
            if nums[ptr2] == nums[ptr1] and (ptr1 - res) & 1 == 0:
                res += 1
                ptr2 += 1
            else:
                ptr1 = ptr2
                ptr2 += 1
        return res if (n - res) & 1 == 0 else res + 1
    
"""
https://leetcode-cn.com/submissions/detail/290113016/

93 / 114 个通过测试用例
状态：解答错误

输入：
[8]
输出：
0
预期：
1
"""
