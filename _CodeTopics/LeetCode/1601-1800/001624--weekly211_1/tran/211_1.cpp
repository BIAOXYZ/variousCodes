class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {

        // 第 211 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/116578019/

        int length = s.size();
        unordered_map<char, vector<int>> dic = {};
        for (int i = 0; i < length; ++i) {
            if ( dic.find(s[i]) != dic.end() ) {
                dic[s[i]].push_back(i);
            } else {
                dic[s[i]] = vector<int>{i};
            }
        }

        int res = -1;
        for (auto& pair : dic) {
            vector<int> vec = pair.second;
            if (vec.size() >= 2) {
                res = max(res, vec.back() - vec[0] - 1);
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/363823368/

执行用时：
0 ms
, 在所有 C++ 提交中击败了
100.00%
的用户
内存消耗：
6.5 MB
, 在所有 C++ 提交中击败了
5.49%
的用户
通过测试用例：
54 / 54
*/
