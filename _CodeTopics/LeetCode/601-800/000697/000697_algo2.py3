class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                dic[num][0] += 1
                dic[num][2] = i
            else:
                dic[num] = [1, i, i]
        
        minLen = len(nums)
        maxFreq = 1
        for currFreq, left, right in dic.values():
            if maxFreq < currFreq:
                maxFreq = currFreq
                minLen = right - left + 1
            elif maxFreq == currFreq:
                # 看了答案的实现，发现python3还能这么搞（计算变量的同时定义变量），所以自己写一下。
                if minLen > (currLen := right - left + 1):
                    minLen = currLen
        return minLen
        
"""
https://leetcode-cn.com/submissions/detail/146940231/

89 / 89 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 16 MB

执行用时：72 ms, 在所有 Python3 提交中击败了79.16%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了18.84%的用户
"""
