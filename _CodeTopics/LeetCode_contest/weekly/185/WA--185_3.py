class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        
        if croakOfFrogs is '':
            return -1
        
        if croakOfFrogs[0] is not 'c':
            return -1
        
        biglist = ['c']
        numberOfFrags = 1
        for i in range(1,len(croakOfFrogs)):
            if croakOfFrogs[i] is 'c':
                biglist.append('c')
                # 判断是否是新青蛙开的'c'
                diff = len(biglist) - biglist.count('croak')
                if diff > numberOfFrags:
                    numberOfFrags = diff
            elif croakOfFrogs[i] is 'r':
                if 'c' in biglist:
                    ind = biglist.index('c')
                    biglist[ind] += 'r'
                else:
                    return -1
            elif croakOfFrogs[i] is 'o':
                if 'cr' in biglist:
                    ind = biglist.index('cr')
                    biglist[ind] += 'o'
                else:
                    return -1
            elif croakOfFrogs[i] is 'a':
                if 'cro' in biglist:
                    ind = biglist.index('cro')
                    biglist[ind] += 'a'
                else:
                    return -1
            else: # 此时croakOfFrogs[i] is 'k':
                if 'croa' in biglist:
                    ind = biglist.index('croa')
                    biglist[ind] += 'k'
                else:
                    return -1
        return numberOfFrags
    
"""
提交结果：解答错误
8 / 54 个通过测试用例
输入："croakcroak"
输出：-1
预期：1
"""
