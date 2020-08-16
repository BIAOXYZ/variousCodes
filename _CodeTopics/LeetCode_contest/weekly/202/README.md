
# 2020.08.16

第 202 场周赛 https://leetcode-cn.com/contest/weekly-contest-202
- 5185. 存在连续三个奇数的数组 https://leetcode-cn.com/contest/weekly-contest-202/problems/three-consecutive-odds/
- 5488. 使数组中所有元素相等的最小操作数 https://leetcode-cn.com/contest/weekly-contest-202/problems/minimum-operations-to-make-array-equal/
- 5489. 两球之间的磁力 https://leetcode-cn.com/contest/weekly-contest-202/problems/magnetic-force-between-two-balls/
- 5490. 吃掉 N 个橘子的最少天数 https://leetcode-cn.com/contest/weekly-contest-202/problems/minimum-number-of-days-to-eat-n-oranges/

# 笔记

## `TLE--202_4.py`

这个程序应该对的，就是plain的动态规划，但是题目里`n`可取的范围太大了导致超时。

## `RE--202_4.py3`

这个之所以突然换成python3是因为要用`functools`里的`lru_cache()`，python2里好像是不能直接用`functools`的。
