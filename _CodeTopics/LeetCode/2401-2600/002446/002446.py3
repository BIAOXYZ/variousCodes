class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        def earlier_than(t1, t2):
            h1, h2 = int(t1[:2]), int(t2[:2])
            m1, m2 = int(t1[3:]), int(t2[3:])
            return h1 < h2 or (h1 == h2 and m1 <= m2)
        return (earlier_than(event1[0], event2[1]) and earlier_than(event2[0], event1[0])) or \
        (earlier_than(event2[0], event1[1]) and earlier_than(event1[0], event2[0]))
        
"""
https://leetcode.cn/submissions/detail/433086510/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
73.03%
的用户
内存消耗：
16.1 MB
, 在所有 Python3 提交中击败了
5.06%
的用户
通过测试用例：
129 / 129
"""
