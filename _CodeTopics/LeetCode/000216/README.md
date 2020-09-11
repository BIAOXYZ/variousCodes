
`216. 组合总和 III` https://leetcode-cn.com/problems/combination-sum-iii/solution/zu-he-zong-he-iii-by-leetcode-solution/
- 方法一：二进制（子集）枚举
  * > 当然，子集枚举也可以用递归实现。在[「官方题解 - 77. 组合」](https://leetcode-cn.com/problems/combinations/solution/zu-he-by-leetcode-solution/)的方法一中提及了子集枚举递归实现的基本框架，感兴趣的同学可以参考。
- [x] 方法二：组合枚举
  * > 这样问题就变成了一个组合枚举问题。组合枚举有两种处理方法——递归法和字典序法，在[「官方题解 - 77. 组合」](https://leetcode-cn.com/problems/combinations/solution/zu-he-by-leetcode-solution/)中有详细的说明。

回溯和回溯优化，以及递归（最好的击败了100%的用户） https://leetcode-cn.com/problems/combination-sum-iii/solution/hui-su-he-hui-su-you-hua-yi-ji-di-gui-zui-hao-de-j/
- > 2，递归解法（没有回溯）
  * > 大家都知道组合使用回溯是最容易解决的，但有没有想过这样一个问题，为什么要使用回溯，不使用回溯能不能解决。之前写过《426，什么是递归，通过这篇文章，让你彻底搞懂递归》的时候提到过，使用回溯是因为list是引用传递，当往回走的时候如果不把之前的值给删除，那么跳到下一个分支的时候就会把之前的值带到下一个分支，导致结果错误，如果list不是引用传递就不会有这个问题了，但怎么才能做到呢，就是新建一个，先画个图看一下

# `000216.py`

对比之前的`39. 组合总和`和`40. 组合总和 II`，这里可以认为供选则的数组`candidates = [1,2,3,4,5,6,7,8,9]`是有序的。这样最后往最终结果`res`里贴某个合法的组合时就不用考虑去重的问题了。

函数`dfs_find_sum_equals_n(currSum, currList, startNum)`仍然有三个参数。其实第一个参数肯定可以通过第二个参数计算出来的（直接sum一下就行），但是每次求和会有些效率损失肯定，而且为了写起code来方便还是多加了这个参数。但是回头可以写个没有这个参数的版本。

语法点：
- 可以用`res.append(currList[:])`替换到之前类似`res.append(copy.deepcopy(currList))`的写法。其实我知道这个语法，就是当时用deepcopy时没想到- -
