class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        n = len(names)
        nextIndexDic = {}
        res = []
        for name in names:
            if name not in nextIndexDic:
                nextIndexDic[name] = 1
                res.append(name)
            else:
                pos = len(name)
                nextInd = nextIndexDic[name]
                tmpName = name + '(' + str(nextInd) + ')'
                while tmpName in nextIndexDic:
                    nextInd += 1
                    suffix = '(' + str(nextInd) + ')'
                    tmpName = tmpName[:pos] + suffix
                nextIndexDic[name] = nextInd + 1
                nextIndexDic[tmpName] = 1
                res.append(tmpName)
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
