class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0)
            return false;
        while (n >= 4) {
            // 擦，昨天 LC231 刚犯过一次，今天又忘了。。。再记一遍：C/C++中 按位与& 的优先级低于 !=
            if ((n & 0b11) != 0) {
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
https://leetcode-cn.com/submissions/detail/182353910/

1061 / 1061 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 5.9 MB

执行用时：4 ms, 在所有 C++ 提交中击败了42.62%的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了22.30%的用户
*/
