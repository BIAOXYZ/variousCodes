class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> res = {first};
        for (auto elem : encoded) {
            res.push_back(elem ^ res.back());
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/175232525/

76 / 76 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 25.2 MB

执行用时：32 ms, 在所有 C++ 提交中击败了71.27%的用户
内存消耗：25.2 MB, 在所有 C++ 提交中击败了47.84%的用户
*/
