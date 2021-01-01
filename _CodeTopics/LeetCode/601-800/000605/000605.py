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
                    if i + 1 <= len(flowerbed) - 1 and flowerbed[i+1] == 1:
                        continue
                    n -= 1
                    flag = 'cannot_plant'
            if n <= 0:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/135186856/

124 / 124 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.7 MB

执行用时：24 ms, 在所有 Python 提交中击败了99.53% 的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了43.57% 的用户
"""
