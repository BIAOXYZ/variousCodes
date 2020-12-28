class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        def isLegal(i, j, k):
            a = b = 0
            for m in range(i,j):
                a ^= arr[m]
            for n in range(j,k+1):
                b ^= arr[n]
            return a == b
            
        length = len(arr)
        numOfLegalArray = 0
        
        for i in range(length-1):
            for j in range(i+1, length):
                for k in range (j, length):
                    if isLegal(i,j,k):
                        numOfLegalArray += 1
        return numOfLegalArray
    
"""
# 跟上一道题提交后情形类似，提交后点“更多明细”啥也没有，服了。看来这周的周赛题目都是这样，辣鸡系统啊。

提交结果：超出时间限制
最后执行的输入：[723,875,440,136,304,271,63,294,281,169,432,185,265,758,1023,760,263,13,266,458,192,774,966,855,145,115,226,233,11,
"""
