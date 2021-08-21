class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        res = []
        stk = []
        for ch in chars:
            if not stk or stk[-1] == ch:
                stk.append(ch)
            else:
                res.append(stk[-1])
                tmpLength = len(stk)
                if tmpLength > 1:
                    for digit in str(tmpLength):
                        res.append(digit)
                stk = [ch]
                ##print res

        ##print "stk is: ", stk
        res.append(stk[-1])
        tmpLength = len(stk)
        if tmpLength > 1:
            for digit in str(tmpLength):
                res.append(digit)

        ##print res
        # 艹了，为什么这句直接赋值不行啊。虽然知道是想考察原地算法，但是我只想先取个巧而已。
        chars = res[:]
        return len(res)
        
"""
https://leetcode-cn.com/submissions/detail/209550374/

12 / 70 个通过测试用例
状态：解答错误

最后执行的输入：
["a","a","b","b","c","c","c"]
输出：
["a","a","b","b","c","c"]
预期结果：
["a","2","b","2","c","3"]
"""
