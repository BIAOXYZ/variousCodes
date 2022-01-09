class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        num0 = nums.count(0)
        if num0 == n or num0 == 0: return 0
        
        indsOfOne = []
        for i, num in enumerate(nums):
            if num == 1:
                indsOfOne.append(i)
        ##print indsOfOne
        
        m = len(indsOfOne)
        dis = [indsOfOne[i] - indsOfOne[i-1] - 1 for i in range(1,m)]
        dis.append(indsOfOne[0] + n - indsOfOne[-1] - 1)
        ##print dis
        
        # 只需要留下最大的distance，剩下的填补
        return sum(dis) - max(dis)
    
"""
https://leetcode-cn.com/submissions/detail/256481284/

18 / 63 个通过测试用例
状态：解答错误

输入：
[1,1,1,0,0,1,0,1,1,0]
输出：
2
预期：
1
"""
