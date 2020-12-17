
# 旧版官方攻略

https://leetcode-cn.com/problems/contains-duplicate/solution/cun-zai-zhong-fu-yuan-su-by-leetcode/
- > 方法一：朴素线性查找 【超时】
  >> 注意: 本方法在 Leetcode 上会超时。一般而言，如果一个算法的时间复杂度为 O(n^2)，它最多能处理 n 大约为 10^4 的数据。当 n 接近 10^5 时就会超时。

# 新版官方攻略

`217. 存在重复元素` https://leetcode-cn.com/problems/contains-duplicate/solution/cun-zai-zhong-fu-yuan-su-by-leetcode-sol-iedd/
- 方法一：排序
- [x] 方法二：哈希表

# 测试用例

```
[1,2,3,1]
[1,2,3,4]
[1,1,1,3,3,4,3,2,4,2]
```

# `000217_algo1.c` --> `deliberate-WA--000217_algo1.c` --> `000217_algo1_impl.c`

`000217_algo1.c`是参照官方答案里`uthash`库的用法写的，没有用到子函数，并且往哈希表里添加元素时可以认为哈希表`dic`是类似“全局变量”的，所以用法上很直观。

然后`deliberate-WA--000217_algo1.c`想用自己封装的子函数来实现，但是发现有问题：如果答案是`false`（比如`[1,2,3,4]`），那么能过；如果答案是`true`（比如`[1,2,3,1]`），那么过不去——看起来是往哈希表里添加元素没添加进去。。。

`000217_algo1_impl.c`修正了`deliberate-WA--000217_algo1.c`的错误，主要原因是`uthash`库往哈希表里添加元素的时候，如果哈希表是个全局变量，那好办；但如果哈希表是当参数传到你封装的函数里，必须用二维指针。。。更具体的参考下面：

`uthash User Guide` -- `Passing the hash pointer into functions` https://troydhanson.github.io/uthash/userguide.html
- > In the example above `users` is a global variable, but what if the caller wanted to pass the hash pointer **into** the `add_user` function? At first glance it would appear that you could simply pass `users` as an argument, but that won’t work right.
  ```c
  /* bad */
  void add_user(struct my_struct *users, int user_id, char *name) {
    ...
    HASH_ADD_INT( users, id, s );
  }
  ```
- > You really need to pass a **pointer** to the hash pointer:
  ```c
  /* good */
  void add_user(struct my_struct **users, int user_id, char *name) { ...
    ...
    HASH_ADD_INT( *users, id, s );
  }
  ```
- > Note that we dereferenced the pointer in the `HASH_ADD` also.
- > The reason it’s necessary to deal with a pointer to the hash pointer is simple: the hash macros modify it (in other words, they modify the **pointer itself** not just what it points to).
