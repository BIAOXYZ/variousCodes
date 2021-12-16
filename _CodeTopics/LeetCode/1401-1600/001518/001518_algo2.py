class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        # 数学：
        # 每次相当于用 numExchange - 1 个空瓶换一瓶纯酒（不带瓶的酒）。
        # 但是最后的那次要注意，有可能空瓶不够换最后一次了。更具体的说：
        # 1. 对于输入9 3，9不断减2，减三次后，最后一次还剩 3，最后还可以再换，所以额外可以喝4瓶；
        # 2. 对于输入15 4，15不断减3，减四次后，最后剩三个空瓶，但是要先有四个空瓶才能换的，所以
        ## 最后一次就换不了了，也就是只能额外喝4瓶，而不是额外喝 15 / 3 == 5 瓶。

        res = numBottles
        if numBottles % (numExchange - 1) != 0:
            res += numBottles / (numExchange - 1)
        else:
            res += numBottles / (numExchange - 1) - 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/249266396/

执行用时：12 ms, 在所有 Python 提交中击败了82.86%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了100.00%的用户
通过测试用例：
64 / 64
"""
