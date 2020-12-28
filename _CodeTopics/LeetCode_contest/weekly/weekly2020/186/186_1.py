class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def countNumber(s,c):
            count = 0
            for i in range(len(s)):
                if s[i] == c:
                    count += 1      
            return count
        
        maxpoint = currpoint = 0
        #for i in range(len(s)):
        #for i in range(1,len(s)-1):
        """
        上面两处浪费了不少时间，第一个注释掉的for是因为至少得给左边分一个字符。第二个注释掉的for错的比较意外：
        末尾那里是不需要再减1的，否则最后剩两位的时候就不走了。"01"就会直接返回0。
        """
        for i in range(1,len(s)):
            currpoint = countNumber(s[:i],'0') + countNumber(s[i:],'1')
            if currpoint > maxpoint:
                maxpoint = currpoint
        return maxpoint
    
"""
103 / 103 个通过测试用例
执行用时：320 ms
内存消耗：12.7 MB
"""
