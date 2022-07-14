class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def get_sign(num):
            return num > 0

        stk = [asteroids[0]]
        n = len(asteroids)
        for i in range(1, n):
            stk.append(asteroids[i])
            # 不是符号不相等就一定会相撞，而是必须靠左的向右飞，靠右的向左飞才会相撞。所以下面这个条件不对。
            # while len(stk) >= 2 and get_sign(stk[-1]) != get_sign(stk[-2]):
            while len(stk) >= 2 and not get_sign(stk[-1]) and get_sign(stk[-2]):
                elem1 = stk.pop(); elem2 = stk.pop()
                if abs(elem1) > abs(elem2):
                    stk.append(elem1)
                elif abs(elem1) < abs(elem2):
                    stk.append(elem2)
        return stk
        
"""
https://leetcode.cn/submissions/detail/336732564/

执行用时：
68 ms
, 在所有 Python3 提交中击败了
12.35%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
55.57%
的用户
通过测试用例：
275 / 275
"""
