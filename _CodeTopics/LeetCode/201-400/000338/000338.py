class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        def number_of_one(n):
            res = 0
            while n:
                if n % 2 == 1:
                    res += 1
                    n = (n-1)/2
                else:
                    n /= 2
            return res
        
        res = [0]
        for i in range(1, num+1):
            res.append(number_of_one(i))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/150390942/

15 / 15 个通过测试用例
状态：通过
执行用时: 188 ms
内存消耗: 17 MB

执行用时：188 ms, 在所有 Python 提交中击败了5.03%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了15.77%的用户
"""
