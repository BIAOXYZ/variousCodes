class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        stackS = []
        for i in range(len(S)):
            if S[i] != "#":
                stackS.append(S[i])
            elif S[i] == "#" and stackS:
                stackS.pop()
            else:
                continue
        stackT = []
        for i in range(len(T)):
            if T[i] != "#":
                stackT.append(T[i])
            elif T[i] == "#" and stackT:
                stackT.pop()
            else:
                continue
        
        return True if stackS == stackT else False
        
"""
https://leetcode-cn.com/submissions/detail/116787236/

110 / 110 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了92.37%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了5.47%的用户
"""
