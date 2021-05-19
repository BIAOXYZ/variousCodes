
`692. 前K个高频单词` https://leetcode-cn.com/problems/top-k-frequent-words/solution/qian-kge-gao-pin-dan-ci-by-leetcode-solu-3qk0/
- [x] 方法一：哈希表 + 排序
- [ ] 方法二：优先队列

# 测试用例

```
["i", "love", "leetcode", "i", "love", "coding"]
2
["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
4
```

# `000692.py3`

排序指南 https://docs.python.org/zh-cn/3/howto/sorting.html || Sorting HOW TO https://docs.python.org/3/howto/sorting.html
- > In Python 3.2, the `functools.cmp_to_key()` function was added to the `functools` module in the standard library.

TODO：这个实现里，要想在 python3 的情况下用 `cmp=` 参数，需要借助上面页面里的`functools.cmp_to_key()`，回头有空再看吧，好累。
