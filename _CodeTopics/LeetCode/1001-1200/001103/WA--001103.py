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
            if currCandy % num_people == 0:
                currCandy += 1 + num_people
            else:
                currCandy += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/116738537/

13 / 27 个通过测试用例
状态：解答错误

输入：
60
4
输出：
[18,12,14,16]
预期：
[15,18,15,12]
"""
