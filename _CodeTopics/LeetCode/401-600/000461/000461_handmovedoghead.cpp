class Solution {
public:
    int hammingDistance(int x, int y) {
        // C++（或C）手动狗头题——Python的这个统计1的个数的函数还真不知道。。。
        return __builtin_popcount(x ^ y);
    }
};

/*
https://leetcode-cn.com/submissions/detail/181183002/

149 / 149 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 5.7 MB

执行用时：4 ms, 在所有 C++ 提交中击败了31.48%的用户
内存消耗：5.7 MB, 在所有 C++ 提交中击败了91.01%的用户
*/
