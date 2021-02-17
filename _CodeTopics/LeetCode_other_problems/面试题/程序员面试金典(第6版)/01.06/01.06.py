class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """

        if not S:
            return S
        res = []
        flag = 0
        
        for i in range(len(S)):
            if flag == 0:
                res.append(S[i])
                flag = 1
            else:
                if S[i] == S[i-1]:
                    flag += 1
                else:
                    res.append(str(flag))
                    res.append(S[i])
                    flag = 1
        res.append(str(flag))
        return ''.join(res) if len(res) < len(S) else S
        
"""
https://leetcode-cn.com/submissions/detail/146254710/

32 / 32 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15.4 MB

执行用时：32 ms, 在所有 Python 提交中击败了97.02%的用户
内存消耗：15.4 MB, 在所有 Python 提交中击败了20.43%的用户
"""
