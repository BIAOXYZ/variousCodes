class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        n = len(boxes)
        res = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    res[i] += abs(i - j)
        return res
        
"""
https://leetcode.cn/submissions/detail/386386942/

执行用时：
5296 ms
, 在所有 Python3 提交中击败了
13.05%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
89.86%
的用户
通过测试用例：
95 / 95
"""
