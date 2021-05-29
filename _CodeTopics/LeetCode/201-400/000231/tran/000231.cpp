class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0)
            return false;
        while (n > 1) {
            if (n % 2 != 0) {
                return false;
            }
            n /= 2;
        }
        return true;
    }
};

/*
https://leetcode-cn.com/submissions/detail/182052845/

1108 / 1108 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 5.8 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：5.8 MB, 在所有 C++ 提交中击败了23.42%的用户
*/
