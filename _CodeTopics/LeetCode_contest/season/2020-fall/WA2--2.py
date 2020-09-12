class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
        
        """
        def binary_search(l, target):
            length = len(l)
            left, right = 0, length - 1
            while left <= right:
                mid = (left + right) / 2
                if l[mid] < target:
                    left = mid + 1
                elif l[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1
                    
        # 看输入规模估计暴力就过不了，直接排序后二分了准备
        lens, lend = len(staple), len(drinks)
        if lens >= lend:
            longer, shorter, lenlonger, lenshorter = staple, drinks, lens, lend
        else:
            longer, shorter, lenlonger, lenshorter = drinks, staple, lend, lens
        
        # res = 0
        # longer.sort()
        # print longer, lens
        # for num in shorter:
        #     print num
        #     obj = x - num
        #     # ind = binary_search(longer, obj)
        #     ind = bisect_right(longer, obj)
        #     res = res + ind
        #     print ind, longer[ind]
        # return res
        """
        
        res = 0
        staple.sort()
        for num in drinks:
            obj = x - num
            ind = bisect_right(staple, obj)
            res = res + ind
        return res
    

"""
https://leetcode-cn.com/contest/season/2020-fall/submissions/107297445/
"""
