
`1486. 数组异或操作` https://leetcode-cn.com/problems/xor-operation-in-an-array/solution/shu-zu-yi-huo-cao-zuo-by-leetcode-solution/
- [x] 方法一：模拟
- [x] 方法二：数学
  * > 记 ⊕ 为异或运算，异或运算满足以下性质：
    + > `∀i ∈ Z`，有 `4i ⊕ (4i+1) ⊕ (4i+2) ⊕ (4i+3) = 0`。

时间复杂度O(1)的公式：数学推导 https://leetcode-cn.com/problems/xor-operation-in-an-array/solution/shu-xue-tui-dao-shi-jian-fu-za-du-o1de-f-b4kk/
- > 由于 `a, a + 2 ,…, a + 2(n−1)` 都只在倒数第二位上进行+1操作，而不涉及最后一位，所以它们最后一位都相同，可以单独把最后一位提出来计算

# 测试用例

```
5
0
4
3
1
7
10
5
```

# 其他

此题是之前第194周周赛第一题：https://leetcode-cn.com/contest/weekly-contest-194/problems/xor-operation-in-an-array/
