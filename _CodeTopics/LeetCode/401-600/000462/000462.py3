class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        # 再想想应该不是取平均数，而是中位数。证明如下（只通过例子说明，不然太长了）：
        # 假定排好序后是 [a,b,c,d,e]，此时不管他们取什么值，最终的目标一定是变成 c 才能使移动次数最少。
        ## 并且此时的移动次数为 c-a + c-b + 0 + d-c + e-c。
        # 否则假定目标是 c+x（c-x 也类似），并且还是在最中间，没有越过右边的任何点，
        ## 此时移动次数为 (c+x-a)+(c+x-b)+x+(d-c-x)+(e-c-x)，可以看出比取中位数多了 x。
        # 如果越过了一些点的话，也是类似的，不过需要一对对分析。比如假定恰好越过了中位数右边第一个点，
        ## 此时移动次数为 (c+x-a)+(c+x-b)+x+(c+x-d)+(e-c-x) --> 因为 c+x 比 d 大了。
        ## (c+x-a) 和 (e-c-x) 相比 c-a 和 e-c 没有变化，(c+x-b) 和 (c+x-d) 相对于 c-b 和 d-c 肯定更大了
        ## 因为 c-b + d-c = d-b，而 c+x 大于 d 了，那么光 (c+x-b) 这部分就已经比原来的 d-b 要大了。
        # 对于偶数长度的数组 [a,b,c,d,e,f] 的分析应该也是类似的，不再赘述。

        n = len(nums)
        nums.sort()
        median = nums[n//2]
        return sum(abs(num - median) for num in nums)
        
"""
https://leetcode.cn/submissions/detail/315356826/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
62.08%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
83.56%
的用户
通过测试用例：
30 / 30
"""
