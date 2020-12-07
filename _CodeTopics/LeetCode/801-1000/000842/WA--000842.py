class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        def backtrack(pos, currArr):
            if pos == length and len(currArr) >= 3:
                # 这里本来的语句是  res = currArr[:]
                # 可不知道为啥返回的res还是空集，
                # 猜测是因为res作用域的问题，直接列表赋值不是全局？只能用这种丑陋的办法先bypass。
                res.append(currArr[:])
                return
            if pos <= length - 1 and S[pos] == '0':
                if len(currArr) < 2:
                    currArr.append(0)
                    backtrack(pos+1, currArr)
                else:
                    if currArr[-1] + currArr[-2] == 0:
                        currArr.append(0)
                        backtrack(pos+1, currArr)
                return
            for end in range(pos+1, length+1):
                if len(currArr) < 2:
                    currArr.append(int(S[pos:end]))
                    backtrack(end, currArr)
                    currArr.pop()
                else:
                    if int(S[pos:end]) > currArr[-1] + currArr[-2]:
                        break
                    elif int(S[pos:end]) == currArr[-1] + currArr[-2]:
                        currArr.append(int(S[pos:end]))
                        backtrack(end, currArr)
                        currArr.pop()
        
        length = len(S)
        res = []
        backtrack(0, [])
        return res[0] if res else []
        
"""
https://leetcode-cn.com/submissions/detail/129391039/

64 / 70 个通过测试用例
状态：解答错误

输入：
"1320581321313221264343965566089105744171833277577"
输出：
[]
预期：
[13205,8,13213,13221,26434,39655,66089,105744,171833,277577]
"""
