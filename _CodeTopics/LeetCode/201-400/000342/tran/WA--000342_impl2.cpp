class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0)
            return false;
        while (n >= 4) {
            if (n & 0b11 != 0) {
                return false;
            }
            n >>= 2;
        }
        if (n == 1) {
            return true;
        } else {
            return false;
        }
    }
};

/*
https://leetcode-cn.com/submissions/detail/182353119/

1035 / 1061 个通过测试用例
状态：解答错误

最后执行的输入：
6
*/
