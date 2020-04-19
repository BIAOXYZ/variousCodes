
# 2020.04.19

第 185 场周赛 https://leetcode-cn.com/contest/weekly-contest-185
- 5388. 重新格式化字符串 https://leetcode-cn.com/contest/weekly-contest-185/problems/reformat-the-string/
- 5389. 点菜展示表 https://leetcode-cn.com/contest/weekly-contest-185/problems/display-table-of-food-orders-in-a-restaurant/
- 5390. 数青蛙 https://leetcode-cn.com/contest/weekly-contest-185/problems/minimum-number-of-frogs-croaking/
- 5391. 生成数组 https://leetcode-cn.com/contest/weekly-contest-185/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

# 笔记

## (1)

【[:star:][`*`]】 偶然想到的了是不是LeetCode的答题界面直接就可以print啊。试了试还真可以。后面简单的排错可以直接做题的页面print，不用搞到ide里了。

```py
# python的str类型判断是否是数字和字符串的方法

s = 'a'
print type(s)
print s.isalpha()
x = '1'
print type(x)
print x.isdigit()
--------------------------------------------------
<type 'str'>
True
<type 'str'>
True
```

思路：先遍历输入字符串s，划分成两个list，一个纯字母一个纯数字。没有选择在初次遍历的时候就直接处理，因为这样做的话还得有额外的存储空间来确认当前的状态，而且到底最后的结果是数字开头还是字母开头只有在遍历完s后才能知道。比如s='abc1234'，想一遍遍历就处理好挺麻烦的。

## (3)

**TODO**: 最开始对每一个非'c'的字符处理是直接在biglist里逐个元素去找有没有对应的前缀，有就把当前字符贴上去，没有就return -1。但是也不知道为啥似乎break老有问题，本地vscode调都有问题。。。

```py
class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        
        if croakOfFrogs is '':
            return -1
        
        if croakOfFrogs[0] is not 'c':
            return -1
        
        biglist = ['c']
        numberOfFrags = 1
        for i in range(1,len(croakOfFrogs)):
            if croakOfFrogs[i] is 'c':
                biglist.append('c')
                numberOfFrags += 1
            elif croakOfFrogs[i] is 'r':
                for element in biglist:
                    if element is 'c':
                        element += 'r'
                        break
                    else:
                        return -1
            elif croakOfFrogs[i] is 'o':
                for element in biglist:
                    if element is 'cr':
                        element += 'o'
                        break
                    else:
                        return -1
            elif croakOfFrogs[i] is 'a':
                for element in biglist:
                    if element is 'cro':
                        element += 'a'
                        break
                    else:
                        return -1
            else: # 此时croakOfFrogs[i] is 'k':
                for element in biglist:
                    if element is 'croa':
                        element += 'k'
                        break
                    else:
                        return -1
        return numberOfFrags
```

