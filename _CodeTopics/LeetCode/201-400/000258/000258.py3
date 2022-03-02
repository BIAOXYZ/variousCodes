class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            tmp = 0
            while num > 0:
                tmp += num % 10
                num //= 10
            num = tmp
        return num
        
"""
执行用时：32 ms, 在所有 Python3 提交中击败了84.22%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了31.18%的用户
通过测试用例：
1101 / 1101
"""
