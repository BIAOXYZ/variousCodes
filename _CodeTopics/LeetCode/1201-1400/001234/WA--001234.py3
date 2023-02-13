class Solution:
    def balancedString(self, s: str) -> int:

        n = len(s)
        ctr = Counter(s)
        absSum = sum(abs(ctr.get(key, 0) - n//4) for key in 'QWER')
        return absSum // 2
        
"""
https://leetcode.cn/submissions/detail/401892093/

15 / 40 个通过测试用例
状态：解答错误

输入：
"WWEQERQWQWWRWWERQWEQ"
输出：
3
预期结果：
4
"""
