class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        length = len(A)
        res = []

        # ord('a')等于97，ord('z')等于122。但是这里直接用，使得代码意义更清晰。
        for i in range(ord('a'), ord('z')+1):
            for j in range(length):
                if A[j].count(chr(i)) == 0:
                    num = 0
                    break
                num = A[0].count(chr(i)) if j == 0 else min(num, A[j].count(chr(i)))
            if num != 0:
                for k in range(num):
                    res.append(chr(i))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/115597431/

83 / 83 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.5 MB

执行用时：32 ms, 在所有 Python 提交中击败了78.21%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了5.61%的用户
"""
