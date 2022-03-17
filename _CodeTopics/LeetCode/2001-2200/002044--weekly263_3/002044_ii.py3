from functools import reduce
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxVal = reduce(lambda x, y : x | y, nums)
        res = 0
        length = len(nums)

        def backtrack(pos, currVal):
            if pos == length:
                return
            nonlocal res
            if currVal | nums[pos] == maxVal:
                res += 1
            backtrack(pos+1, currVal)
            backtrack(pos+1, currVal | nums[pos])
        
        # 可以仔细对比下这个写法为什么就可以不用像 https://leetcode-cn.com/submissions/detail/285058393/
        ## 一样，还得在外面搞个 for 循环。
        # 其实，更想表达的是在回溯算法中，似乎有两大类容易搞混的写法：
        ## 这里的 backtrack(0, 0) 实际意味着：从 pos 为 0 处开始，但是这个位置上的数还没有处理；
        ## 而另外一种写法 backtrack(pos, nums[pos]) 则意味着 backtrack 到当前位置 pos 时，当前位置的值已处理。
        ## 此外可以对比下 if 语句比较条件的不同，仔细想想为什么  -->
        ## 一个是 —— `if currVal | nums[pos] == maxVal:`
        ## 另一个是 —— `if currVal == maxVal:`
        backtrack(0, 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/285058633/

执行用时：432 ms, 在所有 Python3 提交中击败了77.29%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了51.27%的用户
通过测试用例：
111 / 111
"""
