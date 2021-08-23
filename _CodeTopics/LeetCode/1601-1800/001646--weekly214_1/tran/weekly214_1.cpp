class Solution {
public:
    int getMaximumGenerated(int n) {

        // 第 214 场周赛第一题
        // 此前通过的提交：https://leetcode-cn.com/submissions/detail/121813764/

        if (n == 0) return 0;
        if (n == 1) return 1;

        vector<int> tmp(n+1, 0);
        tmp[1] = 1;
        for (int i = 2; i < n+1; ++i) {
            if (i % 2 == 0)
                tmp[i] = tmp[i/2];
            else
                tmp[i] = tmp[i/2] + tmp[i/2 + 1];
        }
        return *max_element(tmp.begin(), tmp.end());
    }
};

/*
https://leetcode-cn.com/submissions/detail/210447717/

101 / 101 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 6.2 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.2 MB, 在所有 C++ 提交中击败了15.00%的用户
*/
