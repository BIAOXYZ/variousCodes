
# 2020.09.06

第 205 场周赛 https://leetcode-cn.com/contest/weekly-contest-205
- 5507. 替换所有的问号 https://leetcode-cn.com/contest/weekly-contest-205/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
- 5508. 数的平方等于两数乘积的方法数 https://leetcode-cn.com/contest/weekly-contest-205/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
- 5509. 避免重复字母的最小删除成本 https://leetcode-cn.com/contest/weekly-contest-205/problems/minimum-deletion-cost-to-avoid-repeating-letters/
- 5510. 保证图可完全遍历 https://leetcode-cn.com/contest/weekly-contest-205/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

# 笔记

## (3)

最近单位VPN出问题了，能连进单位内网，但是谷歌等上不了了。结果我发现repl（ https://repl.it/languages/python ）和Pai（ https://paiza.io/en/languages/python ）这俩网站的Python online IDE竟然也上不去了。。。服了。。。于是只能用这个了（只有Python3，坑）：
https://www.onlinegdb.com/online_python_compiler
```py
i = 0
while i < 5:
    print (i)
    if i == 2:
        i = 4
    else:
        i += 1

# 输出一个字符串中有连续相同字符的字串的下标。
s = 'aaabccefgg'
i = 0
while i < len(s)-1:
    flag = False
    j = i + 1
    while j <= len(s)-1 and s[j] == s[i]:
        flag = True
        j += 1
    if flag:
        print ("i is %d, j is %d" % (i, j-1))
    i = j
--------------------------------------------------
0
1
2
4
i is 0, j is 2
i is 4, j is 5
i is 8, j is 9
```
