class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ctr = collections.Counter(nums)
        keys = ctr.keys()
        maxVal = reduce(lambda x, y: x | y, keys)
        
        # 2**17 = 131072, 2**16 = 65536
        
        # keys.sort(reverse=True)
        # keys2 = [str(bin(key))[2:] for key in keys]
        # maxVal2 = str(bin(maxVal))[2:]
        # print keys2, maxVal2
        
        lis = []
        length = len(keys)
        def backtrack(pos, currArr, currVal):
            ##print pos, currArr, currVal
            if currVal == maxVal:
                lis.append(currArr[:])
                return
            if pos == length:
                return
            for i in range(pos+1, length+1):
                currArr.append(keys[pos])
                backtrack(i, currArr, currVal | keys[pos])
                currArr.pop()
        
        for pos in range(length):
            backtrack(0, [], 0)
        ##print lis
        res = 0
        for l in lis:
            tmp = 1
            for elem in l:
                tmp *= ctr[elem]
            res += tmp
        ##print res
        return res
    
"""
https://leetcode-cn.com/submissions/detail/229626477/

6 / 111 个通过测试用例
状态：解答错误

输入：
[2,2,2]
输出：
3
预期：
7
"""
