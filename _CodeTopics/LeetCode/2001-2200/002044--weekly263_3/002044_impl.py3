from functools import reduce
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        # 前一个写法（ https://leetcode-cn.com/submissions/detail/283285062/ ）
        # 里面的 currArr 根本没有起到任何作用，所以这个里面就把它去掉了。

        maxVal = reduce(lambda x, y : x | y, nums)
        res = [0]
        length = len(nums)

        def backtrack(pos, currVal):
            if currVal == maxVal:
                res[0] += 1
                # 注意这里不能 return！比如第一个数满足了，那后面肯定也都能满足
                # 所以还是要继续往下走——其实应该可以直接算出来吧？回头可以考虑写个优化版。
                # return
            if pos == length:
                return
            for i in range(pos+1, length):
                backtrack(i, currVal | nums[i])
        
        for pos in range(length):
            backtrack(pos, nums[pos])
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/285058393/

执行用时：484 ms, 在所有 Python3 提交中击败了62.94%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了28.34%的用户
通过测试用例：
111 / 111
"""
