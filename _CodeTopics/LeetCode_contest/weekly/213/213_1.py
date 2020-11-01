class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        
        len1, len2 = len(arr), len(pieces)
        used = set()
        for i in range(len1):
            flag = 0
            for j in range(len2):
                len3 = len(pieces[j])
                for k in range(len3):
                    if str(j)+str(k) in used:
                        continue
                    if arr[i] == pieces[j][k]:
                        for t in range(k):
                            if str(j)+str(t) not in used:
                                return False
                        flag = 1
                        used.add(str(j)+str(k))
                        break
                if flag:
                    break
            if not flag:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/120105042/

74 / 74 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 13 MB
"""
