# official
class Solution:
    def sign(self, num: int) -> int:
        return (num > 0) - (num < 0)

    def countSubarrays(self, nums: List[int], k: int) -> int:
        kIndex = nums.index(k)
        ans = 0
        counts = Counter()
        counts[0] = 1
        sum = 0
        for i, num in enumerate(nums):
            sum += self.sign(num - k)
            """
            正确答案这行里是：
                if i < kIndex:
            只是加了个等号改成大于等于就不对了。也就是说 k 本身的 index 只能在左边而不能在右边。
            一个错误用例是：nums = [2,3,1], k = 3。正确结果应该为1，结果输出0。
            """
            if i <= kIndex:
                counts[sum] += 1
            else:
                prev0 = counts[sum]
                prev1 = counts[sum - 1]
                ans += prev0 + prev1
        return ans
"""
https://leetcode.cn/submissions/detail/415198655/

7 / 45 个通过测试用例
状态：解答错误

输入：
[2,3,1]
3
输出：
0
预期结果：
1
"""
