class Solution:
    def binaryGap(self, n: int) -> int:

        posOfOne = []
        currPos = 0
        res = 0
        while n > 0:
            if n & 1 == 1:
                posOfOne.append(currPos)
            currPos += 1
            n >>= 1
        if len(posOfOne) == 1:
            return 0
        return max(posOfOne[i] - posOfOne[i-1] for i in range(len(posOfOne)-1, 0, -1))
        
"""
https://leetcode-cn.com/submissions/detail/304530509/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
70.75%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
52.38%
的用户
通过测试用例：
261 / 261
"""
