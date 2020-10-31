class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        dic, dic2 = {}, {}
        length = len(nums)
        for num in nums:
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
        
        for k, v in dic.items():
            if dic2.has_key(v):
                dic2[v].append(k)
            else:
                dic2[v] = [k]
        
        for i in sorted(dic2.keys()):
            tmplist = dic2[i]
            tmplist.sort(reverse=True)
            for elem in tmplist:
                for j in range(i):
                    res.append(elem)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/120035602/

180 / 180 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
