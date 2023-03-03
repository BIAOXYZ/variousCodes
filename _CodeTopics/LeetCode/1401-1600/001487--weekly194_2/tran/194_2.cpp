class Solution {
public:
    vector<string> getFolderNames(vector<string>& names) {

        // 第 194 场周赛第二题
        // https://leetcode-cn.com/submissions/detail/80893117/
        
        int length = names.size();
        unordered_map<string, int> dic = {};
        vector<string> res;
        for (int i = 0; i < length; ++i) {
            if (dic.find(names[i]) == dic.end()) {
                dic[names[i]] = 1;
                res.push_back(names[i]);
            } else {
                int pos = names[i].size();
                int j = dic[names[i]];
                string tmpname = names[i] + '(' + to_string(j) + ')';
                while (dic.find(tmpname) != dic.end()) {
                    j += 1;
                    string suffix = '(' + to_string(j) + ')';
                    tmpname = tmpname.substr(0, pos) + suffix;
                }
                dic[names[i]] = j + 1;
                dic[tmpname] = 1;
                res.push_back(tmpname);
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/408740312/

执行用时：
152 ms
, 在所有 C++ 提交中击败了
82.49%
的用户
内存消耗：
64.2 MB
, 在所有 C++ 提交中击败了
44.81%
的用户
通过测试用例：
33 / 33
*/
