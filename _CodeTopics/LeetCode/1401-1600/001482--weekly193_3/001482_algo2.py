class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        # 相比trivial的解法，其实离正解也就差一步了。。。而且当时我写trivial解法时还想到了
        # day是从最小值开始好还是从最大值开始好这个问题。。。结果证明是用二分，不然应该都会超时。

        length = len(bloomDay)
        if length < m * k:
            return -1
        elif length == m * k:
            return max(bloomDay)
        
        def has_m_bouquet(day):
            bouquet = 0
            flag = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    flag += 1
                    if flag == k:
                        bouquet += 1
                        if bouquet == m:
                            return True
                        flag = 0
                else:
                    flag = 0
            return False
        
        dayChoices = list(set(bloomDay))
        dayChoices.sort()
        left, right = 0, len(dayChoices) - 1
        while left <= right:
            mid = left + (right - left) / 2
            day = dayChoices[mid]
            if has_m_bouquet(day):
                # 答案的二分查找里while用的是 <，好像确实比 <= 的有优势。如果不是这个赋值，还挺难处理的。
                res = day
                right = mid - 1
            else:
                left = mid + 1
        # MLGB，还以为是Leetcode的Bug，结果搞了半天是return的变量随手写错了。。。小丑竟是我自己。。。
        return res
        
"""
https://leetcode-cn.com/submissions/detail/175908041/

91 / 91 个通过测试用例
状态：通过
执行用时: 700 ms
内存消耗: 28.2 MB

执行用时：700 ms, 在所有 Python 提交中击败了36.36%的用户
内存消耗：28.2 MB, 在所有 Python 提交中击败了9.09%的用户
"""
