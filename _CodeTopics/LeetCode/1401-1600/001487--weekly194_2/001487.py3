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
                # 这里直接从字典里记录的当前最大开始
                j = dic[names[i]]
                tempname = names[i] + '(' + str(j) + ')'
                while dic.has_key(tempname):
                    j += 1
                    suffix = '(' + str(j) + ')'
                    tempname = tempname[:pos] + suffix
                # 更新这个key对应的当前最大
                dic[names[i]] = j + 1
                dic[tempname] = 1
                res.append(tempname)
                ## print "tempname is: ",tempname
        return res
    
"""
https://leetcode.cn/submissions/detail/80893117/

执行用时：
96 ms
, 在所有 Python3 提交中击败了
92.65%
的用户
内存消耗：
31.4 MB
, 在所有 Python3 提交中击败了
10.29%
的用户
通过测试用例：
33 / 33
"""
