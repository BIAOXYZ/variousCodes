class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        indexs, indext = len(S)-1, len(T)-1
        currHashNumS = currHashNumT = 0

        def calculate_comparison_index(arr, currInd, currHashNum):
            while True:
                if currInd == -1:
                    return -1
                if arr[currInd] == '#':
                    currInd -= 1; currHashNum += 1
                else:
                    if currHashNum > 0:
                        currInd -= 1; currHashNum -= 1
                    elif currHashNum == 0:
                        return currInd

        while indexs >= 0 and indext >= 0:
            """
            开始本来用的下面的代码，没有子函数。但是对于 S = "ab##", T = "c#d#" 这种“一下子删到开头”
            的输入解决不了。只能变成子函数的形式。

            # if S[indexs] == '#':
            #     indexs -= 1; currHashNumS += 1
            #     continue
            # else:
            #     if currHashNumS > 0:
            #         indexs -= 1; currHashNumS -= 1
            #         continue
            # if T[indext] == '#':
            #     indext -= 1; currHashNumT += 1
            #     continue
            # else:
            #     if currHashNumT > 0:
            #         indext -= 1; currHashNumT -= 1
            #         continue
            """
            indexs = calculate_comparison_index(S, indexs, currHashNumS)
            indext = calculate_comparison_index(T, indext, currHashNumT)
            if indexs == -1 and indext == -1:
                return True
            if S[indexs] != T[indext]:
                return False
            indexs -= 1; indext -= 1
        
        if indexs == indext:
            return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/117069818/

102 / 110 个通过测试用例
状态：解答错误

输入：
"nzp#o#g"
"b#nzp#o#g"
输出：
false
预期：
true
"""
