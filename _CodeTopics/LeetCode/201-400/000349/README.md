
`349. 两个数组的交集` https://leetcode-cn.com/problems/intersection-of-two-arrays/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode-solution/
- 方法一：两个集合
- 方法二：排序 + 双指针

# 测试用例

```
[1,2,2,1]
[2,2]
[4,9,5]
[9,4,9,8,4]
[1]
[1]
```

# 语法点

python求两个set类型的集合的交集可以用 `A.intersection(B)`，也可以用 `A & B`。

# `WA--000349.py`

偶然失误，可能太累了导致了。range里面明明就应该是`len(nums1)`，不知道为什么会鬼使神差写成`len(nums1)-1`。
