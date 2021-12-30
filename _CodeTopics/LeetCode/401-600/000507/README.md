
`507. 完美数` https://leetcode-cn.com/problems/perfect-number/solution/wan-mei-shu-by-leetcode-solution-d5pw/
- [x] 方法一：枚举
- [ ] 方法二：数学
  * > 根据`欧几里得-欧拉定理`，每个偶完全数都可以写成 $2^{p-1}(2^p-1)$ 的形式，其中 `p` 为素数且 $2^p-1$ 为素数。
  * > 由于目前奇完全数还未被发现，因此题目范围 `[1, 10^8]` 内的完全数都可以写成上述形式。这一共有如下 5 个： `6, 28, 496, 8128, 33550336`
  * 个人补充： 
    + 欧几里得-欧拉定理 https://zh.wikipedia.org/zh-cn/%E6%AD%90%E5%B9%BE%E9%87%8C%E5%BE%97-%E6%AD%90%E6%8B%89%E5%AE%9A%E7%90%86 || Euclid–Euler theorem https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem

```
28
6
496
8128
2

1
```
