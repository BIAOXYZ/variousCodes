class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        n = len(nums)
        prefixMax, prefixMin = [], []
        currMax, currMin = -1, 10**6+1
        for i in range(n):
            currMax = max(currMax, nums[i])
            prefixMax.append(currMax)
        for j in range(n-1, -1, -1):
            currMin = min(currMin, nums[j])
            prefixMin.append(currMin)
        prefixMin.reverse()
        ## print(prefixMax, prefixMin)
        """
        输入：[5,0,3,8,6]
        打印：[5, 5, 5, 8, 8] [0, 0, 3, 6, 6]
        """
        left, right = 0, n-1
        # 写到这里发现可能最简单的贪心就行？
        while left != right and prefixMax[left] <= prefixMin[right]:
            right -= 1
        return right + 1
        
"""
https://leetcode.cn/submissions/detail/376152041/

44 / 66 个通过测试用例
状态：解答错误

输入：
[32,57,24,19,0,24,49,67,87,87]
输出：
6
预期结果：
7
"""
