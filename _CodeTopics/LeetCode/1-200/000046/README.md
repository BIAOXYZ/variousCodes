
`46. 全排列` https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
- [x] 方法一：搜索回溯

回溯算法入门级详解 + 练习（持续更新） https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

回溯算法 https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/

# `deliberate-WA--000046.py`

这个错误的原因是在恢复状态的步骤中，对于当前还可用的数字集合`leftArr`的状态进行恢复时，如果直接append，会把已经用过的那个数字直接贴到list的末尾，造成重复。举个例子，[1,2,3]，第一步选了1，第二步循环中先选了2，然后递归返回后要恢复状态了直接append，`leftArr`就变成了[3,2]。此时循环到下一个num时又选了2，造成重复。

# `000046.py`

修正了上面的错误，每次循环把这个数所在的ind也记一下，恢复状态的时候直接按照ind插入回去。

- 对比下[`000216.py`](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000216/000216.py#L23)可以发现，这次这个题特殊的地方就在于其for循环的list每次会改变，所以不能像[`000216.py`](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000216/000216.py#L23)一样简单的append回去，必须用insert插回原位置。
- 再对比下[`000040_ugly.py`](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000040/000040_ugly.py)，因为`000040_ugly.py`的结果集里的元素（list）不是“必须把所有选择都用一遍”，所以只需append即可。
