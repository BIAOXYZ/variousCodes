class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flag = 'cannot_plant' if flowerbed[0] == 1 else 'ready_to_plant'
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                flag = 'cannot_plant'
            else:
                if flag == 'cannot_plant':
                    flag = 'ready_to_plant'
                elif flag == 'ready_to_plant':
                    n -= 1
                    flag = 'cannot_plant'
            if n <= 0:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/135183990/

108 / 124 个通过测试用例
状态：解答错误

输入：
[1,0,0,0,0,1]
2
输出：
true
预期：
false
"""
