
# 中国时间：2022-06-12 10:30

第 297 场周赛 https://leetcode.cn/contest/weekly-contest-297
- 5259. 计算应缴税款总额 https://leetcode.cn/contest/weekly-contest-297/problems/calculate-amount-paid-in-taxes/
- 5270. 网格中的最小路径代价 https://leetcode.cn/contest/weekly-contest-297/problems/minimum-path-cost-in-a-grid/
- 5289. 公平分发饼干 https://leetcode.cn/contest/weekly-contest-297/problems/fair-distribution-of-cookies/
- 6094. 公司命名 https://leetcode.cn/contest/weekly-contest-297/problems/naming-a-company/

# 其他

感觉这次周赛有了点过去周赛的味道（or 水准？）：第一题也不是秒写就能写出来的，即使不是第四题，什么动态规划、回溯算法该有也都会有的。比如这次，第一题好像用了快半个小时。。。然后第二题dp，第三题回溯。

第三题初看题目很像二分（毕竟确实是求`最小化最大值`的类型），开始也一直按二分想，后面发现不对，因为还有个“搭配”的过程，即使原数组排序了，“搭配”的问题也解决不了。大概差20分钟结束时，看了一眼输入规模，懂了。。。回溯。刚开始想用基于位运算的迭代回溯写法，但是还是不顺，浪费了一些时间。算了，老老实实递归回溯了。
