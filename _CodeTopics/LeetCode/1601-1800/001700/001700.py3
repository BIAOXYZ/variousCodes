class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        remained = [students.count(0), students.count(1)]
        dq = deque(students)
        for sandwich in sandwiches:
            if remained[sandwich] == 0:
                return remained[1-sandwich]
            while dq[0] != sandwich:
                dq.append(dq.popleft())
            remained[sandwich] -= 1
        return 0
        
"""
https://leetcode.cn/submissions/detail/374360410/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
91.70%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
5.19%
的用户
通过测试用例：
55 / 55
"""
