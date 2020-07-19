
`97. 交错字符串` https://leetcode-cn.com/problems/interleaving-string/solution/jiao-cuo-zi-fu-chuan-by-leetcode-solution/
- [x] 方法一：动态规划
  * > **使用滚动数组优化空间复杂度**。 因为这里数组 f 的第 i 行只和第 i - 1 行相关，所以我们可以用滚动数组优化这个动态规划，这样空间复杂度可以变成 O(m)。**敲黑板：我们又遇到「滚动数组」优化啦！不会的同学一定要学习哟。如果还没有做过这几个题建议大家做一下，都可以使用这个思想进行优化**：
    ```
    63. 不同路径 II
    70. 爬楼梯
    剑指 Offer 46. 把数字翻译成字符串
    ```

「手画图解」DFS回溯 及其优化 https://leetcode-cn.com/problems/interleaving-string/solution/shou-hua-tu-jie-dfshui-su-dfsji-yi-hua-by-hyj8/

类似路径问题，找准状态方程快速求解 https://leetcode-cn.com/problems/interleaving-string/solution/lei-si-lu-jing-wen-ti-zhao-zhun-zhuang-tai-fang-ch/

由暴力回溯到记忆化，分享我的动态规划思路 https://leetcode-cn.com/problems/interleaving-string/solution/you-bao-li-hui-su-dao-ji-yi-hua-fen-xiang-wo-de-do/
