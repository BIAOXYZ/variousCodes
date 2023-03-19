class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # 参考官方答案，但是用两个字典分别统计 k 的 index 之前（但是不能包含 k！！！）
        # 和 k 的 index 之后的前缀和。

        def sign(num):
            return (num > 0) - (num < 0)

        kIndex = nums.index(k)
        signs = [sign(num - k) for num in nums]
        prefixSum = list(itertools.accumulate(signs))
        ## print(prefixSum)

        ddicStart, ddicEnd = defaultdict(int), defaultdict(int)
        for i, summ in enumerate(prefixSum):
            if i < kIndex:
                ddicStart[summ] += 1
            else:
                ddicEnd[summ] += 1
        res = 0
        for k, v in ddicStart.items():
            res += ddicEnd[k] + ddicEnd[k+1]
        return res
        
"""
https://leetcode.cn/submissions/detail/415291976/

18 / 45 个通过测试用例
状态：解答错误

输入：
[4,1,3,2]
1
输出：
2
预期结果：
3
"""
