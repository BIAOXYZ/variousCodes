// from: https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/660603

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // 手动狗头题。
        // C++竟然还有这种库函数。。。
        // https://en.cppreference.com/w/cpp/algorithm/next_permutation
        next_permutation(nums.begin(), nums.end());
    }
};

/*
https://leetcode-cn.com/submissions/detail/122280355/

265 / 265 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 12 MB

执行用时：4 ms, 在所有 C++ 提交中击败了93.99%的用户
内存消耗：12 MB, 在所有 C++ 提交中击败了44.07%的用户
*/
