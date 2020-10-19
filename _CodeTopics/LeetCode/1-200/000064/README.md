
`64. 最小路径和` https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-by-leetcode-solution/
- [x] 方法一：动态规划
  >> 注意官方答案里这句，其实我的第一个实现只有`not grid`而少了`not grid[0]`，严格来说是不对的。只是输入的case里没有`[[]]`，所以过了。
  ```py
  if not grid or not grid[0]:
      return 0
  ```

最小路径和 （动态规划，规范流程，清晰图解） https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
>> //notes：这个的特点是“原地dp”，不占用额外空间，故空间复杂度为O(1)。

C 清晰思路 动态规划 https://leetcode-cn.com/problems/minimum-path-sum/solution/cyu-yan-qing-xi-si-lu-by-bella_/

python3 动态规划、深度和广度优先搜索+记忆化 多解法 https://leetcode-cn.com/problems/minimum-path-sum/solution/python3-dong-tai-gui-hua-he-shen-du-you-xian-sou-s/
