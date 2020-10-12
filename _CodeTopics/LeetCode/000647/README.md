
`647. 回文子串` https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/
- [x] 方法一：中心拓展
- [ ] 方法二：Manacher 算法
  * > Manacher 算法是在线性时间内求解最长回文子串的算法。在本题中，我们要求解回文串的个数，为什么也能使用 Manacher 算法呢？这里我们就需要理解一下 Manacher 的基本原理。

Manacher 只会求最长回文子串？太浪费了！ https://leetcode-cn.com/problems/palindromic-substrings/solution/manacher-zhi-hui-qiu-zui-chang-hui-wen-zi-chuan-ta/

# 其他参考链接

【[:star:][`*`]】 Manacher's Algorithm https://www.hackerrank.com/topics/manachers-algorithm + 官方题解里`方法二：Manacher 算法`部分
>> //notes：马拉车算法的核心点其实就是：记录当前所有回文串能达到的最靠右的边界`R`、`R`对应的回文中心`C`和`R`对应的回文左边界`L`（会先对字符串插入一些不存在的字符，从而保证新的串`T`里的回文子串都是奇数长度的）。然后对于每一个新的位置`i`，其在`C`左边有一个关于`C`对称的位置`i'`。以`i'`为回文中心会形成一个回文子串，根据这个回文子串的左边界和`L`的关系会有三种情况，然后依次分析即可。

最长回文子串 https://zh.wikipedia.org/wiki/%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2 || Longest palindromic substring https://en.wikipedia.org/wiki/Longest_palindromic_substring

【LPS (Longest Palindromic Substring) algorithms from www.geeksforgeeks.org 】：
- Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 1 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
  * > We have already discussed Naïve `[O(n^3)]` and quadratic `[O(n^2)]` approaches at [Set 1]() and [Set 2]().
  * > To find Longest Palindromic Substring of a string of length `N`, one way is take each possible `2*N + 1` centers (the `N` character positions, `N-1` between two character positions and `2` positions at left and right ends), do the character match in both left and right directions at each `2*N+ 1` centers and keep track of LPS. This approach takes `O(N^2)` time and that’s what we are doing in [Set 2]().
    >> //notes：(1) 对于中心扩散算法来说，其实遍历`2N-1`个位置就可以了，本题（`LC647`）的官方答案里中心扩散法算法实现部分也是这么用的。因为，以原始字符串第一个字符之前和最后一个字符之后的位置为中心就不可能形成回文子串。 (2) 但是对于马拉车算法，还是要在首尾也插入分隔字符的。
  * > ***Position*** and ***index*** for the string are two different things here. For a given string `S` of length `N`, indexes will be from `0` to `N-1` (total `N` indexes) and positions will be from `0` to `2*N` (total `2*N+1` positions).
  * > LPS length value can be interpreted in two ways, one in terms of index and second in terms of position. LPS value `d` at position `I` (`L[i] = d`) tells that:
    + > Substring from position `i-d` to `i+d` is a palindrome of length `d` (in terms of ***position***)
      > 
    + > Substring from index `(i-d)/2` to `[(i+d)/2 – 1]` is a palindrome of length `d` (in terms of ***index***)
- Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 2 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-2/
- Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 4 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-4/

Manacher’s Algorithm Explained— Longest Palindromic Substring https://medium.com/hackernoon/manachers-algorithm-explained-longest-palindromic-substring-22cb27a5e96f

Manacher's Algorithm - Finding all sub-palindromes in O(N) https://cp-algorithms.com/string/manacher.html

Manacher's Algorithm 马拉车算法 https://www.cnblogs.com/grandyang/p/4475985.html

Longest palindromic substring in O(n) with Manacher's Algorithm https://www.educative.io/edpresso/longest-palindromic-substring-in-on-with-manachers-algorithm

有什么浅显易懂的Manacher Algorithm讲解？ - 知乎 https://www.zhihu.com/question/37289584
- 有什么浅显易懂的Manacher Algorithm讲解？ - windliang的回答 - 知乎 https://www.zhihu.com/question/37289584/answer/465656849
- 有什么浅显易懂的Manacher Algorithm讲解？ - 金天的回答 - 知乎 https://www.zhihu.com/question/37289584/answer/1111317244
  * > geeksforgeeks上有系列文章讲的很清楚。这里借用他们的图解释一下。
    >> Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 1 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
