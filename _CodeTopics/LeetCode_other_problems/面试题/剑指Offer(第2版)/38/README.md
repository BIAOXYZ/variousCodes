
`剑指 Offer 38. 字符串的排列` https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-hhvs/
- [x] 方法一：回溯
- [ ] 方法二：下一个排列
  * > 我们可以这样思考：当我们已知了当前的一个排列，我们能不能快速得到字典序中下一个更大的排列呢？答案是肯定的，参见「[31. 下一个排列的官方题解](https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/)」，当我们已知了当前的一个排列，我们可以在 O(n) 的时间内计算出字典序下一个中更大的排列。这与 C++ 中的 `next_permutation` 函数功能相同。
  * > 具体地，我们首先对给定的字符串中的字符进行排序，即可得到当前字符串的第一个排列，然后我们不断地计算当前字符串的字典序中下一个更大的排列，直到不存在更大的排列为止即可。
  * > 这个方案的优秀之处在于，我们得到的所有排列都不可能重复，这样我们就无需进行去重的操作。同时因为无需使用回溯法，没有栈的开销，算法时间复杂度的常数较小。

[Python] 偷懒使用permutations (一行)，面试记住递归和非递归两种解法 https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/python-permutations-by-qubenhao-3yqy/

# 测试用例

```
"abc"
"xxy"
"mmnn"
```

# 语法点

Python – Itertools.Permutations() https://www.geeksforgeeks.org/python-itertools-permutations/
