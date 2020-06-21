class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        
        length = len(names)
        dic = dict()
        res = []
        for i in range(length):
            if not dic.has_key(names[i]):
                dic[names[i]] = 1
                res.append(names[i])
                ## print "names[i] is: ",names[i]
            else:
                pos = len(names[i])
                j = 1
                tempname = names[i] + '(' + str(j) + ')'
                while dic.has_key(tempname):
                    # 前面顶多有i个重名的，所以到i+1就行。
                    # 另外把后缀是括号1的情况单独处理，否则下面那个tempname[:-3]第一次
                    # 会直接把真正的字符内容给减掉。。。
                    j += 1
                    suffix = '(' + str(j) + ')'
                    tempname = tempname[:pos] + suffix
                dic[tempname] = 1
                res.append(tempname)
                ## print "tempname is: ",tempname
        return res
    
"""
https://leetcode-cn.com/contest/weekly-contest-194/submissions/detail/80747130/

32 / 33 个通过测试用例
	状态：超出时间限制

最后执行的输入： ["p(2)","q","k","q(2)","m","z","b","c(4)(3)","o","v","l(1)(1)","w","u","k(1)(1)","n(1)","l","s(1)","i(1)","p","n"...
"""
