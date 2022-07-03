class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 以排列 [4,5,2,6,3,1] 为例：
        # 寻找最靠右的 index i，满足 nums[i] 右边还有至少一个比它大的数。会找到index 2，也就是数字 2。
        # 在所有比 2 大的数字里寻找最小的那个，这样换过去肯定比大的换过去更小，比如，这里肯定选 3，而不是选 6。
        # 交换后变为 [4,5,3,6,2,1]。
        # 然后再对 index 2 后面的排个序，最后变成 [4,5,3,1,2,6]。

        n = len(nums)
        needChangeInd = -1
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    needChangeInd = i
                    break
        
        needChangeNum = float('inf')
        needChangeInd2 = -1
        for i in range(needChangeInd, n):
            if nums[needChangeInd] < nums[i] < needChangeNum:
                needChangeInd2 = i
                needChangeNum = nums[i]
        
        nums[needChangeInd], nums[needChangeInd2] = nums[needChangeInd2], nums[needChangeInd]
        # Python 的 list 如果想部分排序的话，貌似必须用 sorted，不能用 .sort()。
        # nums[needChangeInd+1:].sort()
        nums[needChangeInd+1:] = sorted(nums[needChangeInd+1:])
        
"""
https://leetcode.cn/submissions/detail/332319595/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
47.70%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
5.20%
的用户
通过测试用例：
265 / 265
"""
