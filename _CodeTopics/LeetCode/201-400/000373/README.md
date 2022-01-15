
`373. 查找和最小的K对数字` https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/solution/cha-zhao-he-zui-xiao-de-kdui-shu-zi-by-l-z526/
- [x] 方法一：优先队列
  * > 本题与「[719. 找出第 k 小的距离对](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)」相似，可以参考该题的解法。
- [ ] 方法二：二分查找
  * > 参考「[378. 有序矩阵中第 K 小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)」的二分查找的解法，我们利用二分查找找到第 kk 小的数对和为 \textit{pairSum}pairSum。

```
[1,7,11]
[2,4,6]
3
[1,1,2]
[1,2,3]
2
[1,2]
[3]
3 
```

# 语法点

- 这道题官方答案优先队列的解法涉及到了堆的自定义比较函数，还没有用过，回头写一遍。也就是在官方答案的写法里，涉及到了 `decltype` —— 有点类似 `auto`，还没有深研究过。
