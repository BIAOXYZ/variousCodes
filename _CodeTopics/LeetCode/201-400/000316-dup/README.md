
`316. 去除重复字母` https://leetcode-cn.com/problems/remove-duplicate-letters/
- > 注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

`316. 去除重复字母` https://leetcode-cn.com/problems/remove-duplicate-letters/solution/qu-chu-zhong-fu-zi-mu-by-leetcode-soluti-vuso/
- [x] 方法一：贪心 + 栈

一招吃遍力扣四道题，妈妈再也不用担心我被套路啦～ https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/
- > 我花了几天时间，从力扣中精选了四道相同思想的题目，来帮助大家解套，如果觉得文章对你有用，记得点赞分享，让我看到你的认可，有动力继续做下去。
- > 这就是接下来要给大家讲的四个题，其中 1081 和 316 题只是换了说法而已。
  ```console
  316. 去除重复字母(困难)
  321. 拼接最大数(困难)
  402. 移掉 K 位数字(中等)
  1081. 不同字符的最小子序列（中等）
  ```
  >> //notes：所以其实这道题过去是hard。。。
  
# 测试用例

```
"bcabc"
"cbacdcbc"
"x"
"xyzyx"
"leetcode"
```

# `WA--000316.py`

这个算法的问题在于：对于"leetcode"的e，先处理了c和d之后，e只能选最后一个，但是实际上考虑到后面那些必须存在的单个字母（比如字母t），e是可以选第一个的。
