
`47. 全排列 II` https://leetcode-cn.com/problems/permutations-ii/solution/quan-pai-lie-ii-by-leetcode-solution/
- [x] 方法一：搜索回溯

回溯搜索 + 剪枝（Java、Python） https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/

47. 全排列 II:【彻底理解排列中的去重问题】详解 https://leetcode-cn.com/problems/permutations-ii/solution/47-quan-pai-lie-iiche-di-li-jie-pai-lie-zhong-de-q/

「手画图解」全排列 II | 利用约束条件充分剪枝 https://leetcode-cn.com/problems/permutations-ii/solution/shou-hua-tu-jie-li-yong-yue-shu-tiao-jian-chong-fe/

# 笔记

官方答案和几个精华的个人答案其实都是用下标而不是用数组本身，所以在他们的答案里都涉及到了一个额外的数组类型的标记变量`vis`（或者`used`）。而至少目前我的`000047.py`系列和`000047_algo2.py`都是直接用数组，所以没有这个问题。
