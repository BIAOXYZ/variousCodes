class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 和`LC78. 子集`的主要区别就是这题的nums里有重复元素。

        se = set()
        def check_if_in_and_add_not_in(lis):
            if tuple(lis) in se:
                return True  
            else:
                se.add(tuple(lis))
                return False
        
        res = [[]]
        length = len(nums)
        
        # 把输入排一下序就可以避免 WA--000090.py 里出现的问题了：[4,4,4,1] 和 [4,4,1,4] 被当成两个不同子集。
        nums.sort()

        def backtrack(currList, startPos):
            if startPos == length:
                return
            for ind in range(startPos, length):
                currList.append(nums[ind])
                if not check_if_in_and_add_not_in(currList):
                    res.append(currList[:])
                    backtrack(currList, ind + 1)
                currList.pop()
        
        backtrack([], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/161979644/

19 / 19 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了75.05%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了55.58%的用户
"""
