from collections import deque
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        n = len(arr)
        i = 0
        dq = deque()
        while i < n:
            if dq:
                if arr[i] != 0:
                    dq.append(arr[i])
                else:
                    dq.append(arr[i])
                    dq.append(arr[i])
                cur = dq.popleft()
                arr[i] = cur
            else:
                if arr[i] == 0:
                    dq.append(0)
            i += 1
        
"""
https://leetcode.cn/submissions/detail/326107927/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
92.14%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
35.35%
的用户
通过测试用例：
30 / 30
"""
