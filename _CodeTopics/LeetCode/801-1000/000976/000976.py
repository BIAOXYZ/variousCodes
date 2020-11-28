class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        A.sort(reverse=True)
        length = len(A)

        # 需要用到贪心思想，不用像前一个超时的做法那样，傻傻的做三重循环。
        # 急着睡觉一时没想到这关节，超时一次才发现。
        for i in range(length-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
        
"""
https://leetcode-cn.com/submissions/detail/127020152/

84 / 84 个通过测试用例
状态：通过
执行用时: 172 ms
内存消耗: 14.5 MB

执行用时：172 ms, 在所有 Python 提交中击败了95.60%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了5.70%的用户
"""
