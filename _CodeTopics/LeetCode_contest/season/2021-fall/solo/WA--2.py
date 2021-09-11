class Solution(object):
    def maxmiumScore(self, cards, cnt):
        """
        :type cards: List[int]
        :type cnt: int
        :rtype: int
        """
        
        if len(cards) < 2:
            return cards[0] if cards[0] % 2 == 0 else 0
        
        arr1, arr2 = [], []
        for card in cards:
            if card % 2 == 1:
                arr1.append(card)
            else:
                arr2.append(card)
        arr1.sort(reverse=True)
        arr2.sort(reverse=True)
        len1, len2 = len(arr1), len(arr2)
        
        res = 0
        ind1, ind2 = 0, 0
        if cnt % 2 == 1:
            if not arr2:
                return 0
            else:
                res += arr2[0]
                ind2 += 1
                cnt -= 1
        
        while cnt > 1:
            sum1 = arr1[ind1] + arr1[ind1 + 1] if ind1 + 1 < len1 else 0
            sum2 = arr2[ind2] + arr2[ind2 + 1] if ind2 + 1 < len2 else 0
            if sum1 >= sum2:
                res += sum1
                ind1 += 2
            else:
                res += sum2
                ind2 += 2
            cnt -= 2
        return res
    
"""
https://leetcode-cn.com/contest/season/2021-fall/submissions/217949096/
"""
