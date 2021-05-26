
`461. 汉明距离` https://leetcode-cn.com/problems/hamming-distance/solution/yi-ming-ju-chi-by-leetcode-solution-u1w7/
- [x] 方法一：内置位计数功能
- [x] 方法二：移位实现位计数
- [x] 方法三：Brian Kernighan 算法
  * > 我们可以使用 `Brian Kernighan` 算法进行优化，具体地，该算法可以被描述为这样一个结论：记 `f(x)` 表示 `x` 和 `x−1` 进行与运算所得的结果（即 `f(x) = x & (x−1)`），那么 `f(x)` 恰为 `x` 删去其二进制表示中最右侧的 1 的结果。
  * > `Brian Kernighan` 算法发布在 1988 年出版的 `The C Programming Language (Second Edition)` 的练习中（由 Brian W. Kernighan 和 Dennis M. Ritchie 编写），但是 Donald Knuth 在 2006 年 4 月 19 日指出，该方法第一次是由 Peter Wegner 在 1960 年的 CACM3 上出版。可以在上述书籍中找到更多位操作的技巧。

# 测试用例

```
1
4
1
6
```
