class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        n = len(arr)
        res = 0
        # 左闭右开
        startPos, endPos = 0, 1
        while endPos <= n:
            currArr = arr[startPos:endPos]
            if sorted(currArr) == list(range(startPos, endPos)):
                res += 1
                startPos = endPos
                endPos += 1
            else:
                endPos += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/372696065/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
15.09%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
92.22%
的用户
通过测试用例：
52 / 52
"""
