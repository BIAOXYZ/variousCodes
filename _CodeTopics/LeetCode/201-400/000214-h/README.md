
`214. 最短回文串` https://leetcode-cn.com/problems/shortest-palindrome/solution/zui-duan-hui-wen-chuan-by-leetcode-solution/
- > 要想找到 s_1，最简单的方法就是暴力地枚举 s_1 的结束位置，并判断其是否是一个回文串。但该方法的时间复杂度为 O(|s|^2)，无法通过本题。因此，我们需要使用更优秀的方法。
- 方法一：字符串哈希
  * > 我们可以用 Rabin-Karp 字符串哈希算法来找出最长的回文串。
  * > 在该方法中，我们将字符串看成一个 base 进制的数，它对应的十进制值就是哈希值。显然，两个字符串的哈希值相等，当且仅当这两个字符串本身相同。然而如果字符串本身很长，其对应的十进制值在大多数语言中无法使用内置的整数类型进行存储。因此，我们会将十进制值对一个大质数 mod 进行取模。
  * > 一般来说，我们选取一个大于字符集大小（即字符串中可能出现的字符种类的数目）的质数作为 base，再选取一个在字符串长度平方级别左右的质数作为 mod，产生哈希碰撞的概率就会很低。
- 方法二：KMP 算法
  * > 如果读者对 KMP 算法不熟悉，可以自行查阅资料进行学习。KMP 算法在笔试或面试中也是非常罕见的考点，读者可以参考[官方题解：459. 重复的子字符串](https://leetcode-cn.com/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/)中的对应部分检验自己的学习成果。
- > 本题也可以用 Manacher 算法找出回文串，但该方法已经达到竞赛难度，读者可以参考[官方题解：5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)中的对应部分汲取一些灵感，并尝试用该算法解决本题。

时间复杂度 O(n) 解法（🐴拉车） https://leetcode-cn.com/problems/shortest-palindrome/solution/shi-jian-fu-za-du-on-jie-fa-la-che-by-time-limit/

图解KMP算法 https://leetcode-cn.com/problems/shortest-palindrome/solution/tu-jie-kmpsuan-fa-by-yangbingjie/
