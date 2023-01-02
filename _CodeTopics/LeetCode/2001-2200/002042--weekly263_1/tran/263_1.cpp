class Solution {
public:
    bool areNumbersAscending(string s) {

        // 第 263 场周赛第一题
        // https://leetcode.cn/submissions/detail/229582321/

        vector<string> l = {};
        stringstream ss(s);
        string str;
        while (ss >> str) {
            l.emplace_back(str);
        }

        vector<string> tmp = {};
        int currNum = 0;
        for (auto token : l) {
            if (isdigit(token[0])) {
                if (stoi(token) > currNum) {
                    currNum = stoi(token);
                } else {
                    return false;
                }
            }
        }
        return true;
    }
};

/*
https://leetcode.cn/submissions/detail/392541479/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
30.38%
的用户
内存消耗：
6.5 MB
, 在所有 C++ 提交中击败了
5.06%
的用户
通过测试用例：
98 / 98
*/
