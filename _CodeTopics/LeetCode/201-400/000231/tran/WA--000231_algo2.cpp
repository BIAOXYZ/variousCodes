class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0)
            return false;
        if (n & n - 1 != 0) {
            return false;
        }
        return true;
    }
};

/*
https://leetcode-cn.com/submissions/detail/182052991/

605 / 1108 个通过测试用例
状态：解答错误

最后执行的输入：
6
*/
/*
运算符优先级的错误，需要加个括号把 n & n - 1 括起来。
*/
