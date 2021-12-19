
# 中国时间：2021-12-19 10:30

第 272 场周赛 https://leetcode-cn.com/contest/weekly-contest-272/
- 5956. 找出数组中的第一个回文字符串 https://leetcode-cn.com/contest/weekly-contest-272/problems/find-first-palindromic-string-in-the-array/
- 5957. 向字符串添加空格 https://leetcode-cn.com/contest/weekly-contest-272/problems/adding-spaces-to-a-string/
- 5958. 股票平滑下跌阶段的数目 https://leetcode-cn.com/contest/weekly-contest-272/problems/number-of-smooth-descent-periods-of-a-stock/
- 5959. 使数组 K 递增的最少操作次数 https://leetcode-cn.com/contest/weekly-contest-272/problems/minimum-operations-to-make-the-array-k-increasing/

# (2)

服了，TM这题肯定没考虑Python的时间，导致一些常用的思路过不了，只能是用不断把s切片，然后加空格再连起来的办法。TM偏偏超时太多次，最后没时间了，淦TMD！

https://leetcode-cn.com/problems/adding-spaces-to-a-string/comments/1289838
- > python写题还是得小心。字符串拼接超时，数组append可以过。
```py
class Solution(object):
    def addSpaces(self, s, spaces):
        ans = ""
        idx = 0
        tmp = list(s)
        for i, k in enumerate(tmp):
            if idx < len(spaces) and i == spaces[idx]:
                idx += 1
                ans += " "
            ans += k
        return ans
```
```py
class Solution(object):
    def addSpaces(self, s, spaces):
        ans = []
        idx = 0
        tmp = list(s)
        for i, k in enumerate(tmp):
            if idx < len(spaces) and i == spaces[idx]:
                idx += 1
                ans.append(' ')
            ans.append(k)
        return "".join(ans)
```
