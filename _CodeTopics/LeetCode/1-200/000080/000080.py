class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 先用简单的搞定了，也就是先不用原地算法。
        if not nums:
            return 0

        tmp = [nums[0]]
        flag = 1
        for i in range(1, len(nums)):
            if nums[i] == tmp[-1]:
                if flag < 2:
                    tmp.append(nums[i])
                    flag += 1
            else:
                tmp.append(nums[i])
                flag = 1
        
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
        
"""
https://leetcode-cn.com/submissions/detail/164130828/

164 / 164 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.8 MB

执行用时：24 ms, 在所有 Python 提交中击败了64.15%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了94.88%的用户
"""
