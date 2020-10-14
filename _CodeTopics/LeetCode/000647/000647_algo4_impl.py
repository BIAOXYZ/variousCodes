class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        len1 = len(s)

        # 构造插入了“#”间隔符的新字符串。注意：这里没有像官方答案一样首尾搞了俩不一样的字符，
        # 而是在后面中心扩散步骤的while循环中，多加了两个简单的判断条件，保证不越界即可。
        # 正常的马拉车算法教程里都没有像答案一样首尾还搞两个不一样的字符。。。
        lis = list(s)
        for i in range(len1 + 1):
            lis.insert(i*2, "#")
        s = "".join(lis)

        res = 0
        len2 = len1 * 2 + 1
        dp = [0 for i in range(len2)]

        rightMost, centerMost = 0, 0
        for i in range(len2):
            if i > rightMost:
                dp[i] = 1
            # 官方答案的这种写法简单粗暴且好记，确实是“做出来这道题”的好办法。但是呢，这样做
            # 忽略了马拉车算法最精华的分析部分，后面会再写一些其他的马拉车算法实现，补上这块。    
            else:
                i_symm = 2*centerMost - i
                ## dp[i] = min(dp[i_symm], rightMost - i + 1)
                ## 官方在中心扩展前对辅助数组的初始化时，就是简单粗暴的用上面那一句，其实还真的没问题。
                ## 不过我们这里要对三种情况（geeksforgeeks是四种情况，但是不如hackerrank的分法好）细分讨论。
                ## Case 1: 以i_symm为中心的回文子串的左边界，在centerMost为中心的回文子串的左边界内部。
                if i_symm - dp[i_symm] > 2*centerMost - rightMost:
                    dp[i] = dp[i_symm]
                ## Case 2: 以i_symm为中心的回文子串的左边界，在centerMost为中心的回文子串的左边界外部。
                elif i_symm - dp[i_symm] < 2*centerMost - rightMost:
                    dp[i] = rightMost - i + 1
                ## Case 3: 这俩的左边界恰好相等。
                else:
                    dp[i] = rightMost - i + 1
            # 开始中心拓展。
            j = 0
            while i-dp[i]-j >= 0 and i+dp[i]+j <= len2-1 and s[i-dp[i]-j] == s[i+dp[i]+j]:
                j += 1
            # 因为最后一次的 j 肯定不对，所以跳出while循环后 j 要再减掉1。
            j -= 1
            dp[i] = dp[i] + j
            if i + dp[i] > rightMost:
                rightMost = i + dp[i]
                centerMost = i
            # 如果只是求最长回文子串，只要返回dp[i]中最大值对应的那个回文子串即可。
            # 这里是求所有回文子串数，所以每次循环都要把本位置形成的新回文子串数加上去。
            res += (dp[i] + 1) / 2
        ##print dp
        return res
        
"""
https://leetcode-cn.com/submissions/detail/115852184/

130 / 130 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.4 MB

执行用时：32 ms, 在所有 Python 提交中击败了97.70%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了41.85%的用户
"""
