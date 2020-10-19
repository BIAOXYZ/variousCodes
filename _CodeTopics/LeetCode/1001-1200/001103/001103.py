class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """

        res = [0 for i in range(num_people)]
        currCandy = 1
        ind = 0

        while candies > 0:
            if candies >= currCandy:
                res[ind] += currCandy
            else:
                res[ind] += candies
            candies -= currCandy
            ind = (ind + 1) % num_people
            currCandy += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/116739972/

27 / 27 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13 MB

执行用时：28 ms, 在所有 Python 提交中击败了47.86%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了5.71%的用户
"""
