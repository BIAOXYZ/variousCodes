class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        strform = big = small = str(num)
        length = len(strform)
        
        """
        replacestr = ''
        for i in range(length):
            if big[i] == '9':
                continue
            else:
                if replacestr == '':
                    replacestr == big[i]
                    big[i] = '9'
                else:
                    if big[i] == replacestr:
                        # python的str是imutable的，所以下面这句会报这个错，改成 big[i] += '9' - big[i] 也是一样   
                        # TypeError: 'str' object does not support item assignment
                        big[i] = '9'
                    else:
                        continue
        
        replacestr = ''
        for i in range(length):
            if small[i] == '0':
                continue
            else:
                if replacestr == '' and small[i] != small[0]:
                    replacestr = small[i]
                    small[i] = '0'
                elif replacestr == '' and small[i] == small[0]:
                    continue
                else:
                    if small[i] == replacestr:
                        small[i] = '0'
                    else:
                        continue
        """
        
        replacestr = ''
        for i in range(length):
            if big[i] == '9':
                continue
            else:
                replacestr = big[i]
                break
        
        if replacestr == '':
            big2 = big
        else:
            big2 = big.replace(replacestr,'9')
        
        replacestr = ''
        replacefirst = False
        for i in range(length):
            if small[0] != '1':
                replacestr = small[0]
                replacefirst = True
                break
            elif small[i] == '0':
                continue
            else:
                if small[i] == small[0]:
                    continue
                else:
                    replacestr = small[i]
                    break
        
        if replacestr == '':
            replacestr = small[0]
            small2 = small.replace(replacestr,'1')
        else:
            if replacefirst == False:
                small2 = small.replace(replacestr,'0')
            else:
                small2 = small.replace(replacestr,'1')
        
        return int(big2) - int(small2)
    
"""
210 / 210 个通过测试用例
	状态：通过
执行用时：24 ms
内存消耗：13 MB
"""
