
转变数组后最接近目标值的数组和 https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/solution/bian-shu-zu-hou-zui-jie-jin-mu-biao-zhi-de-shu-zu-/
- 方法一：枚举 + 二分查找
  ```py
  it = bisect.bisect_left(arr, i)
  ```
- [x] 方法二：双重二分查找

# `001300_algo2.py`笔记

为什么第22行 `while left <= right:` 里的等号不能少：因为left，right都等于3时那一轮也得执行，不然resAns还是默认值9。
```
输入
[4,9,3]
10
输出
3
预期结果
3
stdout
left is:  3
right is:  9
mid is:  6
9
left is:  3
right is:  5
mid is:  4
9
left is:  3
right is:  3
mid is:  3
3

--------------------------------------------------

输入
[4,9,3]
10
输出
9
预期结果
3
stdout
left is:  3
right is:  9
mid is:  6
9
left is:  3
right is:  5
mid is:  4
9
```
