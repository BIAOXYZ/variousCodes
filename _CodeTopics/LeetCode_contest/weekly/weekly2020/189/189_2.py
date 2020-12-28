class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        
        text = text[0].lower() + text[1:]
        length = len(text)
        
        dic = {}
        i = 0
        while i < length:
            if i == length - 1:
                currword = text[i]
                currwordlen = len(currword)
                if dic.has_key(currwordlen):
                    dic[currwordlen].append(currword)
                else:
                    dic[currwordlen] = [currword]
                i = length
                break
            else:
                currword = ''
            for j in range(i+1,length):
                # 必须有这个分支处理最后一个单词，否则会陷入死循环。
                if j == length - 1:
                    currword = text[i:j+1]
                    currwordlen = len(currword)
                    if dic.has_key(currwordlen):
                        dic[currwordlen].append(currword)
                    else:
                        dic[currwordlen] = [currword]
                    # 这一个赋值也不能少，不然break出去还是继续while循环了。
                    i = length
                    break
                # if text[j] != '': 
                # 最开始是上面那句，其实是傻了，空字符和只有一个空格的字符没区分。。。
                if text[j] != ' ':
                    continue
                else:
                    currword = text[i:j]
                    currwordlen = len(currword)
                    if dic.has_key(currwordlen):
                        dic[currwordlen].append(currword)
                    else:
                        dic[currwordlen] = [currword]
                    i = j + 1
                    break
        
        res = ''
        for i in sorted(dic.keys()):
            for elem in dic[i]:
                res = res + ' ' + elem
        # 因为首单词前也会有个空格，所以要去掉一下。
        res = res[1:]
        return res.capitalize()
    
"""
74 / 74 个通过测试用例
	状态：通过
执行用时：8704 ms
内存消耗：19.1 MB
"""
