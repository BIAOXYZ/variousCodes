class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """

        length = len(customers)
        currIncrement = 0
        for i in range(X):
            if grumpy[i] == 1:
                currIncrement += customers[i]
        maxIncrement = currIncrement

        for i in range(X, length):
            if grumpy[i] == 1:
                currIncrement += customers[i]
            if grumpy[i-X] == 1:
                currIncrement -= customers[i-X]
            maxIncrement = max(maxIncrement, currIncrement)
        
        summ = 0
        for i in range(length):
            summ += customers[i] * (1 - grumpy[i])
        return summ + maxIncrement
        
"""
https://leetcode-cn.com/submissions/detail/147796818/

78 / 78 个通过测试用例
状态：通过
执行用时: 252 ms
内存消耗: 14.9 MB

执行用时：252 ms, 在所有 Python 提交中击败了58.82%的用户
内存消耗：14.9 MB, 在所有 Python 提交中击败了70.59%的用户
"""
