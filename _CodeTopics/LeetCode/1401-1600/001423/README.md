
`1423. 可获得的最大点数` https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/solution/ke-huo-de-de-zui-da-dian-shu-by-leetcode-7je9/
- [x] 方法一：滑动窗口

# 测试用例

```
[1,2,3,4,5,6,1]
3
[2,2,2]
2
[9,7,7,9,7,7,9]
7
[1,1000,1]
1
[1,79,80,1,1,1,200,1]
3
[9,7,7,9,7,7,9]
5
```

# 语法点

C++ `<numeric>` 里的 `accumulate()` 函数，刷题时用来替代python的内置函数 `sum()`。但是注意这个函数的参数至少要多一个，必须有一个初始值。`001423.cpp`里的两处用法分别是：
```cpp
int total = accumulate(cardPoints.begin(), cardPoints.end(), 0);
```
```cpp
int currSum = accumulate(cardPoints.begin(), cardPoints.begin() + n, 0);
```
