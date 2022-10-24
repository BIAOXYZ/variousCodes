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
        print(prefixMax, prefixMin)
        """
        输入：[5,0,3,8,6]
        打印：[5, 5, 5, 8, 8] [0, 0, 3, 6, 6]
        """
        for ind in range(n-1):
            if prefixMax[ind] <= prefixMin[ind+1]:
                return ind+1
        
"""
https://leetcode.cn/submissions/detail/376155119/

执行用时：
516 ms
, 在所有 Python3 提交中击败了
12.87%
的用户
内存消耗：
25.9 MB
, 在所有 Python3 提交中击败了
44.23%
的用户
通过测试用例：
66 / 66
"""
