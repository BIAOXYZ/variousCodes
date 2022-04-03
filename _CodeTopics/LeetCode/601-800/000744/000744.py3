class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if target >= letters[-1]:
            return letters[0]
        
        n = len(letters)
        resInd = -1
        left, right = 0, n-1
        while left <= right:
            mid = left + ((right - left) // 2)
            if letters[mid] > target:
                right = mid - 1
            elif letters[mid] <= target:
                left = mid + 1
                resInd = max(resInd, mid)
        return letters[resInd+1]
        
"""
https://leetcode-cn.com/submissions/detail/294338136/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
55.64%
的用户
内存消耗：
16.7 MB
, 在所有 Python3 提交中击败了
76.32%
的用户
通过测试用例：
165 / 165
"""
