class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {

        // 第 35 场双周赛第一题： https://leetcode-cn.com/submissions/detail/109623827/

        int length = arr.size();
        int res = 0;
        for (int currlen = 1; currlen < length + 1; currlen += 2) {
            for (int i = 0; i < length - currlen + 1; ++i) {
                for (int k = i; k < i + currlen; ++k) {
                    res += arr[k];
                }
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/212713159/

96 / 96 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 8 MB

执行用时：4 ms, 在所有 C++ 提交中击败了76.28%的用户
内存消耗：8 MB, 在所有 C++ 提交中击败了87.21%的用户
*/
