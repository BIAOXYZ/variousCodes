class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        while (n > 0) {
            if (n % 2 != 0) {
                res += 1;
            }
            n /= 2;
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/188947622/

601 / 601 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 5.9 MB

执行用时：4 ms, 在所有 C++ 提交中击败了39.40%的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了52.96%的用户
*/
