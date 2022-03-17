
`2044. 统计按位或能得到最大值的子集数目` https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets/solution/tong-ji-an-wei-huo-neng-de-dao-zui-da-zh-r6zd/
- [x] 方法一：位运算
- [x] 方法二：回溯

```
[3,1]
[2,2,2]
[3,2,1,5]
```

# 笔记

【[:star:][`*`]】 注意对比 `002044_impl.py3` 和 `002044_ii.py3`，看看 backtrack 时，对于当前位置 pos 上的数 nums[pos] **已经处理过了** 和 **还没有处理** 的区别！

# 语法点

Python 的 `or_` 函数。
