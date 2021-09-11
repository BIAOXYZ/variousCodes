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
        arr1.sort()
        arr2.sort()
        
        """
        # 开始想用动态规划，后来发现不是
        
        dp1 = [0] * (cnt + 1)
        dp2 = [0] * (cnt + 1)
        if arr2:
            dp[1] = arr2[-1]
            arr2.pop()
        if arr2:
            dp[2] = arr2[-1]
            arr2.pop()
        for i i range(3, cnt+1):
            if i % 2 == 1:
                dp[i] = 
        """
        
        res = 0
        if cnt % 2 == 1:
            if not arr2:
                return 0
            else:
                res += arr2[-1]
                arr2.pop()
                cnt -= 1
        
        while cnt > 1:
            if len(arr1) >= 2 and len(arr2) >= 2:
                sum1 = arr1[-1] + arr1[-2]
                sum2 = arr2[-1] + arr2[-2]
                if sum1 >= sum2:
                    res += sum1
                    arr1.pop(); arr1.pop()
                else:
                    res += sum2
                    arr2.pop(); arr2.pop()
                cnt -= 2
            elif len(arr1) < 2 and len(arr2) >= 2:
                # 这里其实可以break出去，直接一直加偶数数组的数加到尾了，不过还是算了，写简单点。
                sum2 = arr2[-1] + arr2[-2]
                res += sum2
                arr2.pop(); arr2.pop()
                cnt -= 2
            elif len(arr1) >= 2 and len(arr2) < 2:
                sum1 = arr1[-1] + arr1[-2]
                res += sum1
                arr1.pop(); arr1.pop()
                cnt -= 2
        return res
    
"""
https://leetcode-cn.com/contest/season/2021-fall/submissions/217943955/
"""
