class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def get_sign(num):
            return num > 0

        stk = [asteroids[0]]
        n = len(asteroids)
        for i in range(1, n):
            stk.append(asteroids[i])
            while len(stk) >= 2 and get_sign(stk[-1]) != get_sign(stk[-2]):
                elem1 = stk.pop(); elem2 = stk.pop()
                if abs(elem1) > abs(elem2):
                    stk.append(elem1)
                elif abs(elem1) < abs(elem2):
                    stk.append(elem2)
        return stk
        
"""
https://leetcode.cn/submissions/detail/336727776/

143 / 275 个通过测试用例
状态：解答错误

输入：
[-2,-1,1,2]
输出：
[]
预期结果：
[-2,-1,1,2]
"""
