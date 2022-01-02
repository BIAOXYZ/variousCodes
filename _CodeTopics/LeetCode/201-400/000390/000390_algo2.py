class Solution:
    def lastRemaining(self, n: int) -> int:
        
        # 参考官方答案，不一样的只是等差数列的首元素和尾元素是用两个变量分别表示。

        start, end = 1, n
        total, diff = n, 1
        roundFlag = 1
        while total > 1:
            if roundFlag:
                if total & 1 == 1:
                    start += diff
                    end -= diff
                else:
                    start += diff
                    # end = end
            else:
                if total & 1 == 1:
                    start += diff
                    end -= diff
                else:
                    # start = start
                    end -= diff
            roundFlag ^= 1
            diff <<= 1
            total >>= 1
        return start
        
"""
https://leetcode-cn.com/submissions/detail/254380981/

执行用时：32 ms, 在所有 Python3 提交中击败了97.76%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了31.34%的用户
通过测试用例：
3377 / 3377
"""
