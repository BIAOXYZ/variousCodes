
# 中国时间：2021-12-12 10:30

第 271 场周赛 https://leetcode-cn.com/contest/weekly-contest-271/
- 5952. 环和杆 https://leetcode-cn.com/contest/weekly-contest-271/problems/rings-and-rods/
- 5953. 子数组范围和 https://leetcode-cn.com/contest/weekly-contest-271/problems/sum-of-subarray-ranges/
- 5954. 给植物浇水 II https://leetcode-cn.com/contest/weekly-contest-271/problems/watering-plants-ii/
- 5955. 摘水果 https://leetcode-cn.com/contest/weekly-contest-271/problems/maximum-fruits-harvested-after-at-most-k-steps/

# (4) 

又是差了一点，但是在 posfruit 字典里删key的做法是不对的，会影响其他记忆化搜索分支。PS：手误写错了，函数名称虽然是 backtrack，其实想表达的是记忆化搜索。

```
[[2,8],[6,3],[8,6]]
5
4
[[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
5
4
[[0,3],[6,4],[8,5]]
3
2

[[0,10000]]
200000
200000

[[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]]
21
30
```
