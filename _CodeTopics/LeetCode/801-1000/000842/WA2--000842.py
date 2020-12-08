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
https://leetcode-cn.com/submissions/detail/129474680/

65 / 70 个通过测试用例
状态：解答错误

输入：
"539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
输出：
[539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
预期：
[]
"""
