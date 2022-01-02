class Solution:
    def lastRemaining(self, n: int) -> int:
        
        # 这个应该会超时，但是主要是把 list 切片的知识再复习下。

        arr = list(range(1, n+1))
        flag = 1
        while len(arr) > 1:
            if flag:
                arr = arr[1::2]
            else:
                if len(arr) % 2 == 0:
                    arr = arr[::2]
                else:
                    arr = arr[1::2]
            flag ^= 1
        return arr[0]
        
"""
https://leetcode-cn.com/submissions/detail/254303508/

3375 / 3377 个通过测试用例
状态：超出时间限制

最后执行的输入：
100000000
"""
