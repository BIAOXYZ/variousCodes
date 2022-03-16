class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        for bitmap in range(1 << n):
            currSubset = []
            for i in range(n):
                # 如果下面的 if 语句用这句： `if bitmap & (1 << i) == 1:`，
                ## 那么答案将会是 [[],[1],[],[1],[],[1],[],[1]]，
                # 也就是只有不进入 if 分支的空集和子集 [1] 会被记录。
                # 所以这里只是非零，而不是等于 1。
                if bitmap & (1 << i):
                    currSubset.append(nums[i])
            res.append(currSubset[:])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/283938769/

执行用时：32 ms, 在所有 Python3 提交中击败了82.55%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了86.68%的用户
通过测试用例：
10 / 10
"""
