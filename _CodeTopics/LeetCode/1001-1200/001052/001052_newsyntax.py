class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """

        # 和前一个区别不大：就是把求初始的 currIncrement 和 summ 部分换成了用sum函数加zip的两种形式：一种带if，一种不带。

        length = len(customers)
        maxIncrement = currIncrement = sum(cust * isGrumpy for cust, isGrumpy in zip(customers[:X], grumpy[:X]))

        for i in range(X, length):
            if grumpy[i] == 1:
                currIncrement += customers[i]
            if grumpy[i-X] == 1:
                currIncrement -= customers[i-X]
            maxIncrement = max(maxIncrement, currIncrement)
        
        summ = sum(cust for cust, isGrumpy in zip(customers, grumpy) if isGrumpy == 0)
        return summ + maxIncrement
        
"""
https://leetcode-cn.com/submissions/detail/147798711/

78 / 78 个通过测试用例
状态：通过
执行用时: 260 ms
内存消耗: 16.1 MB

执行用时：260 ms, 在所有 Python 提交中击败了41.18%的用户
内存消耗：16.1 MB, 在所有 Python 提交中击败了5.88%的用户
"""
"""
用了zip()感觉内存消耗急剧上升，应该是申请了额外的空间。
"""
