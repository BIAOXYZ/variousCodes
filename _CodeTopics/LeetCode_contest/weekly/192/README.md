
# 2020.06.07

第 192 场周赛 https://leetcode-cn.com/contest/weekly-contest-192
- 5428. 重新排列数组 https://leetcode-cn.com/contest/weekly-contest-192/problems/shuffle-the-array/
- 5429. 数组中的 k 个最强值 https://leetcode-cn.com/contest/weekly-contest-192/problems/the-k-strongest-values-in-an-array/
- 5430. 设计浏览器历史记录 https://leetcode-cn.com/contest/weekly-contest-192/problems/design-browser-history/
- 5431. 给房子涂色 III https://leetcode-cn.com/contest/weekly-contest-192/problems/paint-house-iii/

# 笔记

## (2)

思路：
- 首先这题的输入数组arr肯定要排序，不然怎么知道中位数是哪个。
- 本来想的是原始数组排序后，其中的每一个数都和中位数做差并求绝对值，存到一个结果数组absArr里。
- 然后用max函数，absArr里当前最大值的ind（下标）找到，并从arr里根据ind把真正的数取出来贴到结果数组里。一次取出一个，并且对这两个数组的同一个位置都用pop。
- **但是这个方法还是有缺点**：arr=[1,1,3,5,5]，k=2。会得出absArr=[2,2,0,2,2]，但是最后返回的两个值都是1，也就是用max的时候，可能负的比较多，但是结果应该是正的优先。
- 最后想了想把absArr做成一个这样的列表：[[差的绝对值,原始值]]。对于这样一个列表absArr，排序的话首先会根据每个元素（一个只有两个元素的列表）的第一个值排，然后第一个值相等的再根据第二个排。这样只要sort的时候让reverse=True就是大的在前了。
```py
l = [[2,1],[1,2],[1,1]]
l.sort()
print l
l.sort(reverse=True)
print l
--------------------------------------------------
[[1, 1], [1, 2], [2, 1]]
[[2, 1], [1, 2], [1, 1]]
```
