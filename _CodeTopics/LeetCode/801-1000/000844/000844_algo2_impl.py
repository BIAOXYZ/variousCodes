class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        indexs, indext = len(S)-1, len(T)-1
        currHashNumS = currHashNumT = 0

        # def calculate_comparison_index(arr, currInd, currHashNum):
        #     while True:
        #         if currInd == -1:
        #             return -1
        #         if arr[currInd] == '#':
        #             currInd -= 1; currHashNum += 1
        #         else:
        #             if currHashNum > 0:
        #                 currInd -= 1; currHashNum -= 1
        #             elif currHashNum == 0:
        #                 return currInd

        while indexs >= 0 and indext >= 0:
            if S[indexs] == '#':
                indexs -= 1; currHashNumS += 1
                continue
            else:
                if currHashNumS > 0:
                    indexs -= 1; currHashNumS -= 1
                    continue
            if T[indext] == '#':
                indext -= 1; currHashNumT += 1
                continue
            else:
                if currHashNumT > 0:
                    indext -= 1; currHashNumT -= 1
                    continue
            """
            这次不用这个子函数了。
            # indexs = calculate_comparison_index(S, indexs, currHashNumS)
            # indext = calculate_comparison_index(T, indext, currHashNumT)
            """
            if indexs == -1 or indext == -1:
                break
            if S[indexs] != T[indext]:
                return False
            indexs -= 1; indext -= 1
        
        def strictly_empty_string(s):
            ind, powerLetter, powerHash = len(s)-1, 0, 0
            while ind >= 0:
                if s[ind] == '#':
                    powerHash += 1
                else:
                    powerLetter += 1
                ind -= 1
                if powerHash < powerLetter:
                    return False
            return True

        if indexs == indext:
            return True
        elif indexs == -1 and strictly_empty_string(T[:indext+1]):
            return True
        elif indext == -1 and strictly_empty_string(S[:indexs+1]):
            return True
        else:
            return False
        
"""
https://leetcode-cn.com/submissions/detail/117087046/

110 / 110 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB

执行用时：28 ms, 在所有 Python 提交中击败了25.11%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了5.94%的用户
"""
