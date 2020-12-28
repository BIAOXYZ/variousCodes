class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        insertnum = 0
        totalsum = 0
        for i in range(length):
            if s[i] == ')':
                totalsum -= 1
            elif totalsum < 0 and s[i] == '(':
                totalsum = abs(totalsum)
                insertnum = insertnum + totalsum / 2 + 2*(totalsum % 2)
                totalsum = 2
            else:
                totalsum += 2
        
        # 这个大于0的分支要放在小于0那个之前，不然输入 ")))))))" 输出为12，而不是5。
        # 因为totalsum从-7变成7，相当于多算了一遍。。。
        if totalsum > 0:
            insertnum += totalsum
        if totalsum < 0:
            totalsum = abs(totalsum)
            insertnum = insertnum + totalsum / 2 + 2*(totalsum % 2)
        return insertnum
    
"""
https://leetcode-cn.com/submissions/detail/96087751/

58 / 102 个通过测试用例
	状态：解答错误

输入： "(()))(()))()())))"
输出： 1
预期： 4
"""
