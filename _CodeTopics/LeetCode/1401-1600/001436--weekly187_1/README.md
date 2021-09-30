
`1436. 旅行终点站` https://leetcode-cn.com/problems/destination-city/solution/lu-xing-zhong-dian-zhan-by-leetcode-solu-pscd/
- [x] 方法一：哈希表

# 测试用例

```
[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
[["B","C"],["D","B"],["C","A"]]
[["A","Z"]]
[["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
```

# 语法

C++ `unordered_map` 的几种遍历方法。其实主要就两大类：通过 `std::pair<keyType, valueType>` 和 `std::unordered_map<keyType, valueType>::iterator`。

【[:star:][`*`]】 最值得一记的是在 `cppreference` 官方 `unordered_map` 页面 （ https://en.cppreference.com/w/cpp/container/unordered_map ） 发现了另外一种此前没见过的全新的遍历方法，而且效率似乎还特别高。具体情况可以参见 [`187_1_v.cpp`](./tran/187_1_v.cpp)。

# 其他

曾经的第 187 周周赛第一题。
