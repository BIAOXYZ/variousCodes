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
                tempname = names[i] + '(1)'
                while dic.has_key(tempname):
                    # 前面顶多有i个重名的，所以到i+1就行。
                    # 另外把后缀是括号1的情况单独处理，否则下面那个tempname[:-3]第一次
                    # 会直接把真正的字符内容给减掉。。。
                    for j in range(2,i+1):
                        suffix = '(' + str(j) + ')'
                        ##print suffix
                        tempname = tempname[:-3] + suffix
                dic[tempname] = 1
                res.append(tempname)
                ## print "tempname is: ",tempname
        return res
    
"""
https://leetcode-cn.com/contest/weekly-contest-194/submissions/detail/80726955/

9 / 33 个通过测试用例
	状态：解答错误


输入： ["r","y","m","o(3)(2)","f","r","z","u","w","q(2)(3)","a","s","k","o","y","b","n","t(2)(4)","s","e","r","v","g","q(1)(4)","j","j","r(4)(4)","t"]
输出： ["r","y","m","o(3)(2)","f","r(1)","z","u","w","q(2)(3)","a","s","k","o","y(1)","b","n","t(2)(4)","s(1)","e","r(((((((((((20)","v","g","q(1)(4)","j","j(1)","r(4)(4)","t"]
预期： ["r","y","m","o(3)(2)","f","r(1)","z","u","w","q(2)(3)","a","s","k","o","y(1)","b","n","t(2)(4)","s(1)","e","r(2)","v","g","q(1)(4)","j","j(1)","r(4)(4)","t"]
"""
