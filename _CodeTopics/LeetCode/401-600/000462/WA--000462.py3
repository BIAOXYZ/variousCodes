class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        # 变换完成后，最终最优的数就是变成 avg，avg+1，avg-1 三种情况。
        # 如果能整除，只有 avg 就可以了。否则应该还需要算算另外两个。

        n = len(nums)
        avg = sum(nums) // n
        return min(sum(abs(num - t) for num in nums) for t in [avg-1, avg, avg+1])
        
"""
https://leetcode.cn/submissions/detail/315352945/

16 / 30 个通过测试用例
状态：解答错误

输入：
[1,0,0,8,6]
输出：
15
预期结果：
14
"""
