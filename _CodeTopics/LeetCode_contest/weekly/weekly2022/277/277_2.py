class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        tmp1, tmp2 = [], []
        for num in nums:
            if num > 0:
                tmp1.append(num)
            else:
                tmp2.append(num)
        # 可能用zip就能直接搞定？但是比赛里还是先写出来再说了。。。
        res = []
        for i in range(len(tmp1)):
            res.append(tmp1[i])
            res.append(tmp2[i])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/261450081/

133 / 133 个通过测试用例
状态：通过
执行用时: 220 ms
内存消耗: 46.4 MB
"""
