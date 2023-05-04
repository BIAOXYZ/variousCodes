class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        # 如果用动态规划，一个核心点就是标识当前状态。
        # 目前没想到什么特别好的办法，就是用 “最左侧的b” 和 “最右侧的a” 两个 index 来标识。
        # 一旦 “最左侧的b” >= “最右侧的a” 了，说明字符串已经平衡了；否则，按照贪心思想，就是
        ## 两种思路，一种是换掉最左边的 b，一种是换掉最右边的 a。

        n = len(s)
        memoDic = {}
        def memorize_search(leftmost_b, rightmost_a):
            if leftmost_b >= rightmost_a:
                return 0
            if key := (leftmost_b, rightmost_a) in memoDic:
                return memoDic[key]
            
            next_leftmost_b = s.find('b', leftmost_b + 1)
            if next_leftmost_b == -1:
                next_leftmost_b = n - 1
            next_rightmost_a = rightmost_a - 1
            while next_rightmost_a > 0 and s[next_rightmost_a] != 'a':
                next_rightmost_a -= 1
            
            memoDic[key] = 1 + min(memorize_search(next_leftmost_b, rightmost_a), memorize_search(leftmost_b, next_rightmost_a))
            return memoDic[key]
        
        leftmost_b, rightmost_a = 0, n - 1
        while leftmost_b < n and s[leftmost_b] != 'b':
            leftmost_b += 1
        while rightmost_a > 0 and s[rightmost_a] != 'a':
            rightmost_a -= 1
        return memorize_search(leftmost_b, rightmost_a)
        
"""
https://leetcode.cn/submissions/detail/429798231/

6 / 157 个通过测试用例
状态：超出时间限制

最后执行的输入：
"baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb"
"""
