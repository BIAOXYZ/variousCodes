
# 2020.05.24

第 190 场周赛 https://leetcode-cn.com/contest/weekly-contest-190
- 5416. 检查单词是否为句中其他单词的前缀 https://leetcode-cn.com/contest/weekly-contest-190/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
- 5417. 定长子串中元音的最大数目 https://leetcode-cn.com/contest/weekly-contest-190/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
- 5418. 二叉树中的伪回文路径 https://leetcode-cn.com/contest/weekly-contest-190/problems/pseudo-palindromic-paths-in-a-binary-tree/
- 5419. 两个子序列的最大点积 https://leetcode-cn.com/contest/weekly-contest-190/problems/max-dot-product-of-two-subsequences/

# 笔记

## (1)

第一题把整个输入字符串sentence按空格分隔成一个一个单词，其实可以直接用python字符串的split方法，但是觉得自己写比较好。
```

```

## (2)

- 第二题先用最基本的办法，输入字符串s的下标从0开始（对应的当前单词为`s[0:k]`），到最后一个**可能的起始下标**length-k（对应的当前单词为`s[length-k:length-1]`），每次都考察当前k长字串里元音字符的个数并和maxVowel比较。这个方法不好的地方就是每次小循环也要处理k次是不是元音字符的比较，结果超时了。。。
- 后来改成了`190_2_algo2.py`里的算法，先把第一个k长子串的currVowel和整个的maxVowel都求出来，然后对于s里的每个新字符，只是比较首尾字符是不是元音字符的情况。
