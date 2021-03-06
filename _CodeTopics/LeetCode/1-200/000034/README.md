
`34. 在排序数组中查找元素的第一个和最后一个位置` https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/
- [x] 方法一：二分查找

【[:star:][`*`]】 关于 while (left <= right) 写法返回值的详细讨论 https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/da-jia-bu-yao-kan-labuladong-de-jie-fa-fei-chang-2/

一文带你搞定二分查找及其多个变种 https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/yi-wen-dai-ni-gao-ding-er-fen-cha-zhao-j-ymwl/

34.【朴实无华的二分查找】咱们一步一步来！ https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/34po-shi-wu-hua-de-er-fen-cha-zhao-zan-men-yi-bu-y/

# 测试用例

```
[5,7,7,8,8,10]
8
[5,7,7,8,8,10]
6
[]
0
[1]
1
[1]
2
[1,2,2,2,3]
2
```

# `000034_algo2_template.py`

官方答案的实现虽然简洁，但是时间长了不是那么好重复理解和无bug写出的。感觉还是我这个实现（在一段时间后）更好写些，因为和plain版本的二分查找差别很小。
