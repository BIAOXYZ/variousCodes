
# 2021-01-03 10:30

第 222 场周赛 https://leetcode-cn.com/contest/weekly-contest-222
- 5641. 卡车上的最大单元数 https://leetcode-cn.com/contest/weekly-contest-222/problems/maximum-units-on-a-truck/
- 5642. 大餐计数 https://leetcode-cn.com/contest/weekly-contest-222/problems/count-good-meals/
- 5643. 将数组分成三个子数组的方案数 https://leetcode-cn.com/contest/weekly-contest-222/problems/ways-to-split-array-into-three-subarrays/
- 5644. 得到子序列的最少操作次数 https://leetcode-cn.com/contest/weekly-contest-222/problems/minimum-operations-to-make-a-subsequence/

# (2)

`WA--222_2.py`错是因为在本题里1也算2的次幂。。。所以一旦有0和1，0+1也算。。。

`WA--222_2_algo2.py`的错误原因还没有深究，反正用了个取巧的办法bypass了：把结果res分成两部分，一部分是不同的num（比如1和3）的计数，由于计算了两遍，最后要除2；另一部分就是num和num本身，如果符合条件就计数，并且这个不用最后除2.
