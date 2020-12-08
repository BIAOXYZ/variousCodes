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
            # 上一个答案（WA--000842.py）出错应该是因为这个if分支里少了两处currArr.pop()。
            if pos <= length - 1 and S[pos] == '0':
                if len(currArr) < 2:
                    currArr.append(0)
                    backtrack(pos+1, currArr)
                    currArr.pop()
                else:
                    if currArr[-1] + currArr[-2] == 0:
                        currArr.append(0)
                        backtrack(pos+1, currArr)
                        currArr.pop()
                return
            for end in range(pos+1, length+1):
                # 还有这个条件：数不能超过 2**31-1，忘了。。。
                if int(S[pos:end]) > 2**31-1:
                    break
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
https://leetcode-cn.com/submissions/detail/129478469/

70 / 70 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.4 MB

执行用时：36 ms, 在所有 Python 提交中击败了59.65%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了5.26%的用户
"""
