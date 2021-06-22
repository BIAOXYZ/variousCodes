
`剑指 Offer 15. 二进制中1的个数` https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/er-jin-zhi-zhong-1de-ge-shu-by-leetcode-50bb1/
- [x] 方法一：循环检查二进制位
- [x] 方法二：位运算优化

# 测试用例

```
00000000000000000000000000001011
00000000000000000000000010000000
11111111111111111111111111111101
```

# `15_algo2.py`

还是熟悉的 `n & n - 1` 等于抹掉 n 最低位的 1 这个trick，已经见过不少次了，不再赘述。真要参考就 `LC231` 吧，比这个还复杂一丢丢貌似，而且C++版本的几乎也都写了。 
