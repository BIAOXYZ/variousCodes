
`216. 组合总和 III` https://leetcode-cn.com/problems/combination-sum-iii/solution/zu-he-zong-he-iii-by-leetcode-solution/
- 方法一：二进制（子集）枚举

# `000216.py`

对比之前的`39. 组合总和`和`40. 组合总和 II`，这里可以认为供选则的数组`candidates = [1,2,3,4,5,6,7,8,9]`是有序的。这样最后往最终结果`res`里贴某个合法的组合时就不用考虑去重的问题了。

函数`dfs_find_sum_equals_n(currSum, currList, startNum)`仍然有三个参数。其实第一个参数肯定可以通过第二个参数计算出来的（直接sum一下就行），但是每次求和会有些效率损失肯定，而且为了写起code来方便还是多加了这个参数。但是回头可以写个没有这个参数的版本。

语法点：
- 可以用`res.append(currList[:])`替换到之前类似`res.append(copy.deepcopy(currList))`的写法。其实我知道这个语法，就是当时用deepcopy时没想到- -
