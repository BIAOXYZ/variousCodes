
`743. 网络延迟时间` https://leetcode-cn.com/problems/network-delay-time/solution/wang-luo-yan-chi-shi-jian-by-leetcode-so-6phc/
- [x] 方法一：Dijkstra 算法

五种最短路径算法总结 https://leetcode-cn.com/problems/network-delay-time/solution/dirkdtra-by-happysnaker-vjii/

# 测试用例

```
[[2,1,1],[2,3,1],[3,4,1]]
4
2
[[1,2,1]]
2
1
[[1,2,1]]
2
2

[[1,2,1],[2,1,3]]
2
2

[[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]]
5
1
```

# `000743_algo2.py`

我觉得这道题不算特别典型的最短路径题目，至少不能当模版题。然后之前在力扣唯一一次做最短路径还是 231 周周赛第三题。这里（大概）参考了下当时的代码（当时超时了- -）和网上查的攻略。然后凭印象写了一把。过了，并且速度还比较快。但是和官方答案的实现方式很不一样——虽然还没有细看，但是官方答案一上来就申请了个二维列表，就这点就肯定不一样。

- https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode_contest/weekly/weekly2021/231/README.md#3
  * 《图解：最短路径之迪杰斯特拉算法》 https://mp.weixin.qq.com/s/vYEu2kXv_FLWHozfEfsZcw
