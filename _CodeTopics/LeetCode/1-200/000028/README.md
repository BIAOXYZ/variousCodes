
`28. 实现 strStr()` https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode-solution-ds6y/
- > **前言**
  * > 本题是经典的字符串单模匹配的模型，因此可以使用字符串匹配算法解决，常见的字符串匹配算法包括暴力匹配、Knuth-Morris-Pratt 算法、Boyer-Moore 算法、Sunday 算法等，本文将讲解 Knuth-Morris-Pratt 算法。
  * > 因为哈希方法可能出现哈希值相等但是字符串不相等的情况，而 strStr 函数要求匹配结果必定正确，因此本文不介绍哈希方法，有兴趣的读者可以自行了解滚动哈希的实现（如 Rabin-Karp 算法）。
- [x] 方法一：暴力匹配
- [ ] 方法二：Knuth-Morris-Pratt 算法

Sunday 解法 https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/

【动画模拟】这可能是全网最细的 KMP 讲解！（BF,BM,KMP） https://leetcode-cn.com/problems/implement-strstr/solution/zhe-ke-neng-shi-quan-wang-zui-xi-de-kmp-8zl57/

「代码随想录」KMP算法详解 https://leetcode-cn.com/problems/implement-strstr/solution/bang-ni-ba-kmpsuan-fa-xue-ge-tong-tou-ming-ming-ba/

# 测试用例

```
"hello"
"ll"
"aaaaa"
"bba"
""
""
"helloworld"
"world"

"mississippi"
"issip"
```
