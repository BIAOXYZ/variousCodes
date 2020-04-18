
# 2020.04.18

第 24 场双周赛 https://leetcode-cn.com/contest/biweekly-contest-24
- 5372. 逐步求和得到正数的最小值 https://leetcode-cn.com/contest/biweekly-contest-24/problems/minimum-value-to-get-positive-step-by-step-sum/
- 5373. 和为 K 的最少斐波那契数字数目 https://leetcode-cn.com/contest/biweekly-contest-24/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
- 5374. 长度为 n 的开心字符串中字典序第 k 小的字符串 https://leetcode-cn.com/contest/biweekly-contest-24/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
- 5375. 恢复数组 https://leetcode-cn.com/contest/biweekly-contest-24/problems/restore-the-array/

# 笔记

## (3)

思路：首先先把首字母判断出来，因为首字母是有三种情况的，比较特殊。首字母之后的字符串只可能有两种情况（按照“大”和“小”处理就好——比如若此时最后一位是'b'，则下一位“大”的情况就是'c'，“小”的情况就是'a'），这部分在while循环里处理。但是遗憾的是本想通过字符转ascii码从而能统一处理，也就是不用管之前resStr最后一个字符是啥都能直接处理。但结果还是没搞成，最后还是要再判断一层。不过这俩python内置函数当知识点记一下吧。

```py
print ord('a')
print chr(97)
--------------------------------------------------
97
a
```
