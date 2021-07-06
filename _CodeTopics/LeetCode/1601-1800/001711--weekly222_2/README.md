
`1711. 大餐计数` https://leetcode-cn.com/problems/count-good-meals/solution/da-can-ji-shu-by-leetcode-solution-fvg9/
- [x] 方法一：哈希表

# 测试用例

```
[1,3,5,7,9]
[1,1,1,3,3,3,7]
```

# 其他

1. 此题是之前第 222 周周赛第二题。
2. 这道题很好的诠释了：“**trivial的二重for循环会超时，但是利用一些特殊的特征（比如26个字母，10个数字之类的  -->  具体到这道题是符合条件的和都是2的若干次幂，但是可能性很少）可以基本只用一重for循环搞定**。”
