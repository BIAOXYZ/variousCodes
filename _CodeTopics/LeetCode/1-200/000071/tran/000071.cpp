class Solution {
public:
    string simplifyPath(string path) {
        
        // 官方答案里用的是下面两行不给初始值的方式来分别初始化 vector 和 string。
        // 但是我后面用赋初始值的形式，也没啥影响。
        vector<string> stk;
        string curr;
        for (char ch : path) {
            if (ch == '/') {
                if (curr.empty())
                    curr = "/";
                else if (curr.back() == '/')
                    continue;
                else {
                    stk.push_back(curr);
                    curr = "/";
                }
            } else {
                curr += ch;
            }
        }
        if (curr != "/")
            stk.push_back(curr);

        vector<string> tmp = {};
        for (auto subpath : stk) {
            if (subpath == "/.")
                continue;
            else if (subpath == "/..") {
                if (!tmp.empty())
                    tmp.pop_back();
            } else {
                tmp.push_back(subpath);
            }
        }

        string res = "";
        for (auto subpath : tmp){
            res += subpath;
        }

        if (!res.empty())
            return res;
        else
            return "/";
    } 
};

/*
https://leetcode-cn.com/submissions/detail/255415177/

执行用时：4 ms, 在所有 C++ 提交中击败了88.71%的用户
内存消耗：8.7 MB, 在所有 C++ 提交中击败了64.02%的用户
通过测试用例：
256 / 256
*/
