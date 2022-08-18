class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        # 第 189 场周赛第一题
        # 手动狗头题
        return sum(startTime[i] <= queryTime <= endTime[i] for i in range(len(startTime)))
        
"""
https://leetcode.cn/submissions/detail/352092352/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
86.69%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
96.04%
的用户
通过测试用例：
111 / 111
"""
