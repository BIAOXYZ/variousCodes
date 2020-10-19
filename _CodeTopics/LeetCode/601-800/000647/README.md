
`647. 回文子串` https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/
- [x] 方法一：中心拓展
- [x] 方法二：Manacher 算法
  * > Manacher 算法是在线性时间内求解最长回文子串的算法。在本题中，我们要求解回文串的个数，为什么也能使用 Manacher 算法呢？这里我们就需要理解一下 Manacher 的基本原理。

Manacher 只会求最长回文子串？太浪费了！ https://leetcode-cn.com/problems/palindromic-substrings/solution/manacher-zhi-hui-qiu-zui-chang-hui-wen-zi-chuan-ta/

# 测试用例

```console
"abc"
"aaa"
"abababa"
"abaaba"
"cdbabcbabdbab"
"babcbabcbaccba"

dp数组：
[0, 1, 0, 1, 0, 1, 0]
[0, 1, 2, 3, 2, 1, 0]
[0, 1, 0, 3, 0, 5, 0, 7, 0, 5, 0, 3, 0, 1, 0]
[0, 1, 0, 3, 0, 1, 6, 1, 0, 3, 0, 1, 0]
[0, 1, 0, 1, 0, 1, 0, 3, 0, 1, 0, 9, 0, 1, 0, 3, 0, 1, 0, 7, 0, 1, 0, 3, 0, 1, 0]
[0, 1, 0, 3, 0, 1, 0, 7, 0, 1, 0, 9, 0, 1, 0, 5, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 0]

回文子串数：
3
6
16
11
23
25
```

# 其他参考链接

【[:star:][`*`]】 Manacher's Algorithm https://www.hackerrank.com/topics/manachers-algorithm 【1】 + 官方题解里`方法二：Manacher 算法`部分 【2】
>> //notes：马拉车算法的核心点其实就是：记录当前所有回文串能达到的最靠右的边界`R`、`R`对应的回文中心`C`和`R`对应的回文左边界`L`（会先对字符串插入一些不存在的字符，从而保证新的串`T`里的回文子串都是奇数长度的）。然后对于每一个新的位置`i`，其在`C`左边有一个关于`C`对称的位置`i'`。以`i'`为回文中心会形成一个回文子串，根据这个回文子串的左边界和`L`的关系会有三种情况，然后依次分析即可。
- > Case 1: The length of the longest palindrome centered at `i'` is such that the left boundary of the palindrome does not extend beyond or until the left boundary of the longest palindrome centered at `C`.
- > Case 2: Consider that the palindrome centred at `i'` extends beyond the left boundary of the palindrome centred at `C`.
- > Case 3: In this case, The left boundary of the palindrome centred at `i'` is the same as the left boundary of the palindrome centred at `C`.

------------------------------------------------------------------------------------------------------------------------------------------------------

>> //notes：下面的【3】和【4】讲得更细致，不过【4】最后分了四个case，其实不如【1】里的三种情况更清楚（【2】就更不用说了，对实现马拉车算法最有优势，写法最简单粗暴）。
>>
>> 此外，【3】和【4】里的图都特别棒，并且更清楚地阐明了辅助数组里`f[i]`（我用的符号是`dp[i]`）的概念：就是表示以`i`为中心的最长**全字符回文子串**的长度（所有这些`dp[i]`中的最大值其实就是待求的最长回文子串的长度，也记为`LPS(Longest Palindromic Substring)`）。这个值也等价于以`i`为中心的（**但是不包含`i`**）最长回文子串的半径。
>>
>> 以字符串`"abababa"`为例，插入分隔符`|`后变为`"|a|b|a|b|a|b|a|"`。考虑最中间那个`b`，它在七号位置。我们很容易看出来，`dp[7]`的值为`7`。这里的长度`7`可以认为是：
- 以七号位置的字符`b`为中心的，最长**全字符回文子串**`"abababa"`的长度，也就是`LSP`的值。
- 以七号位置的字符`b`为中心的（**但是不包含`b`**），最长回文子串的半径`|a|b|a|`的长度，也就是`R`的值。

想一想为什么这两个值一定是相等的？由于插入了间隔符，所有原始字符串中的回文子串，在新字符串中与其对应的那个回文子串的长度都是奇数（基本上任何一个讲马拉车算法的攻略，开头都会提到这个事实）。前面`"abababa"`的情形很容易看出来，我们不妨再以下图中第二个字符串`"abaaba"`为例：其变换后为`"|a|b|a|a|b|a|"`，以中间相邻的那对`aa`为中心的回文子串——也就是以最中间的`|`为中心的回文子串——也就是整个新串——其长度为`13`，照样是奇数。

那么我们可以假定**全字符回文子串的左半边**（如果这个全字符回文子串是奇数长度，那么这里的“左半边”不包括最中间的那个字符）的长度为`k`。
于是有:
1. 如果中心是字符，比如`"|a|b|a|b|a|b|a|"`，中心是字符`b`，此时有`LSP = 2k+1`。由上面的假设也就是`len("aba") = k`，由于这个`k`长的部分要被`k+1`个分隔符包围（在这个例子中，也就是形成`"|a|b|a|"`），所以半径为：`R = k + (k+1) = 2k + 1`，也就是`LSP = R`。
2. 如果中心是分隔符（对应着原字符串中偶数长度的回文子串），比如`"|a|b|a|a|b|a|"`，中心是字符`|`，此时有`LSP = 2k`。同样的分析，由于中心的分隔符`|`不能算（因为半径`R`不包括中心），所以一共要补`k`个`|`，此时`R`也等于`2k`。故同样有`LSP = R`。

`"abababa"`
- ![](https://media.geeksforgeeks.org/wp-content/uploads/ltp3.jpg)  ![](https://media.geeksforgeeks.org/wp-content/uploads/ltp5.jpg)

`"abaaba"`
- ![](https://media.geeksforgeeks.org/wp-content/uploads/ltp4.jpg)  ![](https://media.geeksforgeeks.org/wp-content/uploads/ltp5.jpg)

【LPS (Longest Palindromic Substring) algorithms from www.geeksforgeeks.org 】：
- Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 1 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/ 【[:star:][`*`]】【3】
  * > We have already discussed Naïve `[O(n^3)]` and quadratic `[O(n^2)]` approaches at [Set 1]() and [Set 2]().
  * > To find Longest Palindromic Substring of a string of length `N`, one way is take each possible `2*N + 1` centers (the `N` character positions, `N-1` between two character positions and `2` positions at left and right ends), do the character match in both left and right directions at each `2*N+ 1` centers and keep track of LPS. This approach takes `O(N^2)` time and that’s what we are doing in [Set 2]().
    >> //notes：(1) 对于中心扩散算法来说，其实遍历`2N-1`个位置就可以了，本题（`LC647`）的官方答案里中心扩散法算法实现部分也是这么用的。因为，以原始字符串第一个字符之前和最后一个字符之后的位置为中心就不可能形成回文子串。 (2) 但是对于马拉车算法，还是要在首尾也插入分隔字符的。
  * > ***Position*** and ***index*** for the string are two different things here. For a given string `S` of length `N`, indexes will be from `0` to `N-1` (total `N` indexes) and positions will be from `0` to `2*N` (total `2*N+1` positions).
  * > LPS length value can be interpreted in two ways, one in terms of index and second in terms of position. LPS value `d` at position `I` (`L[i] = d`) tells that:
    + > Substring from position `i-d` to `i+d` is a palindrome of length `d` (in terms of ***position***)
      > 
    + > Substring from index `(i-d)/2` to `[(i+d)/2 – 1]` is a palindrome of length `d` (in terms of ***index***)
- Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 2 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-2/ 【[:star:][`*`]】【4】
  * > **Case 1**: L[currentRightPosition] = L[currentLeftPosition] applies when:
  * > **Case 2**: L[currentRightPosition] = L[currentLeftPosition] applies when:
  * > **Case 3**: L[currentRightPosition] > = L[currentLeftPosition] applies when:
  * > **Case 4**: L[currentRightPosition] > = centerRightPosition – currentRightPosition applies when:
    >> //notes：其实这里严格来讲应该是等于而不是大于等于，因为`左回文的左边界`超出了`中心回文的左边界`，意味着`右回文的右边界`在扩散时，其右边一旦超出`中心回文的右边界`，立刻就会不匹配。
- Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 4 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-4/

------------------------------------------------------------------------------------------------------------------------------------------------------

最长回文子串 https://zh.wikipedia.org/wiki/%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2 || Longest palindromic substring https://en.wikipedia.org/wiki/Longest_palindromic_substring

Manacher’s Algorithm Explained— Longest Palindromic Substring https://medium.com/hackernoon/manachers-algorithm-explained-longest-palindromic-substring-22cb27a5e96f

Manacher's Algorithm - Finding all sub-palindromes in O(N) https://cp-algorithms.com/string/manacher.html

Manacher's Algorithm 马拉车算法 https://www.cnblogs.com/grandyang/p/4475985.html

Longest palindromic substring in O(n) with Manacher's Algorithm https://www.educative.io/edpresso/longest-palindromic-substring-in-on-with-manachers-algorithm

有什么浅显易懂的Manacher Algorithm讲解？ - 知乎 https://www.zhihu.com/question/37289584
- 有什么浅显易懂的Manacher Algorithm讲解？ - windliang的回答 - 知乎 https://www.zhihu.com/question/37289584/answer/465656849
- 有什么浅显易懂的Manacher Algorithm讲解？ - 金天的回答 - 知乎 https://www.zhihu.com/question/37289584/answer/1111317244
  * > geeksforgeeks上有系列文章讲的很清楚。这里借用他们的图解释一下。
    >> Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 1 https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
