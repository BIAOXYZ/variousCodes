from functools import reduce
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        # 第 263 场周赛第三题。
        # 当时没做出来，还是因为想复杂了，直接普通的回溯就可以了应该。

        maxVal = reduce(lambda x, y : x | y, nums)
        res = [0]
        length = len(nums)

        def backtrack(pos, currArr, currVal):
            if currVal == maxVal:
                res[0] += 1
                # 注意这里不能 return！比如第一个数满足了，那后面肯定也都能满足
                # 所以还是要继续往下走——其实应该可以直接算出来吧？回头可以考虑写个优化版。
                # return
            if pos == length:
                return
            for i in range(pos+1, length):
                currArr.append(nums[i])
                backtrack(i, currArr, currVal | nums[i])
                currArr.pop()
        
        for pos in range(length):
            backtrack(pos, [], nums[pos])
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/283285062/

执行用时：616 ms, 在所有 Python3 提交中击败了51.47%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了84.56%的用户
通过测试用例：
111 / 111
"""
