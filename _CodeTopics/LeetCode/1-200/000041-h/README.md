
41. 缺失的第一个正数 https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/
- [x] 方法一：哈希表
- [x] 方法二：置换

另外还实现了一个不同于方法一和方法二的算法（`000041_algo3.py`），目前讨论区没看到有人提出类似的。尽管worst-case time complexity不是线性的，但是实际跑的情况来看比绝大多数线性的都快。。。而且思想和写法也都更简单。主要是受了官方答案里这个图的启发：**既然那些0和负数都要处理，那我为什么不能直接删掉？如果0和负数（是对最终答案无用的，所以）可以删，那么每一轮所有大于length的正整数也是无用的**。然后沿着这个思想就可以了。
![](https://assets.leetcode-cn.com/solution-static/41/41_fig1.png)
