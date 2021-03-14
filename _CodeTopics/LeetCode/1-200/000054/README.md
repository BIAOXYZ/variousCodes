
`54. 螺旋矩阵` https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/
- 方法一：模拟
- [x] 方法二：按层模拟

# 测试用例

```
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
```

# `000054_optm.cpp`

## 语法点： `ERROR: AddressSanitizer: negative-size-param`

直接参见 `000054_optm.cpp` 文件里的注释吧，总之就是迭代器用错了导致的。是从下面这个帖子的回答里得到了启发。
- What's wrong with this?  Please help! https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/389931/whats-wrong-with-this-please-help
  * > `q.end()` does not return a iterator to the last element of the vector. It would return an iterator past the end element of the vector. You can find more details in the link http://www.cplusplus.com/reference/vector/vector/end/
  * > If you change the `q.erase(q.end())` to `q.pop_back()` it should work fine.

不过好像 [`[RE]--000705_algo2.cpp`](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/601-800/000705/tran/%5BRE%5D--000705_algo2.cpp) 的错还是和这个不一样，回头再看了。
