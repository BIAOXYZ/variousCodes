class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        
        # 这篇文章（ https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/solution/you-ji-qiao-de-mei-ju-chang-shu-you-hua-daxit/ ）里，
        # 通过集合的方式来解释常用的位运算技巧 `subSet = (subSet - 1) & complementSet`，感觉挺生动的。

        ctr = Counter(num1 & num2 for num1 in nums for num2 in nums)
        res = 0
        for num in nums:
            complementSet = num ^ 0xffff
            subSet = complementSet
            while subSet >= 0:
                if subSet in ctr:
                    res += ctr[subSet]
                subSet = (subSet - 1) & complementSet
                # 此时已经转了一圈了，所以可以退出去了。
                # 注意当 subset 为 0 时，减去 1 后变成 -1，相当于全 1，所以再和 complementSet 做
                # 与运算并不会导致负数出现。。。想以负数为条件 break 出去是不行的，开始这里踩坑了。
                if subSet == complementSet:
                    break
        return res
        
"""
https://leetcode.cn/submissions/detail/409327625/

执行用时：
620 ms
, 在所有 Python3 提交中击败了
76.58%
的用户
内存消耗：
18.2 MB
, 在所有 Python3 提交中击败了
77.93%
的用户
通过测试用例：
25 / 25
"""
