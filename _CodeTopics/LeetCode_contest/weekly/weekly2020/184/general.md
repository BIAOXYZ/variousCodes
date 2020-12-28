
# 2020.04.12

第 184 场周赛 https://leetcode-cn.com/contest/weekly-contest-184
- 5380. 数组中的字符串匹配 https://leetcode-cn.com/contest/weekly-contest-184/problems/string-matching-in-an-array/
- 5381. 查询带键的排列 https://leetcode-cn.com/contest/weekly-contest-184/problems/queries-on-a-permutation-with-key/
- 5382. HTML 实体解析器 https://leetcode-cn.com/contest/weekly-contest-184/problems/html-entity-parser/
- 5383. 给 N x 3 网格图涂色的方案数 https://leetcode-cn.com/contest/weekly-contest-184/problems/number-of-ways-to-paint-n-x-3-grid/

# 笔记

## (2)

开始就想用list，后来觉得会不会效率太低，就想着用链表。然后想了想链表得维护当前节点的position，每次也都是整个链表都得动，还不如list。<br>于是在代码里把链表相关的code注释掉了，但是开头自己添加的定义`Class Node`忘注释掉了，但是程序也没问题直接AC（**可见除了在Solution类的母方法下添加子函数之外，也可以自己添加符合语法规则的类**）。
