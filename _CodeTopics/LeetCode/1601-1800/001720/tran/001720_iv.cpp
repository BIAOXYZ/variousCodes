class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> res(1, first);
        for (auto elem : encoded) {
            // 同理 *(res.end()-1) 也可以换成 *res.rbegin()。
            res.push_back(elem ^ *res.rbegin());
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/175239236/

76 / 76 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 25.4 MB

执行用时：40 ms, 在所有 C++ 提交中击败了27.00%的用户
内存消耗：25.4 MB, 在所有 C++ 提交中击败了24.25%的用户
*/
