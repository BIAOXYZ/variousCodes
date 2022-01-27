class Solution {
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) {

        // 第 257 场周赛第二题
        // https://leetcode-cn.com/submissions/detail/215334740/
        // 但是觉得比赛时的代码是有小问题的，因此参考了：
        // https://leetcode-cn.com/submissions/detail/263040972/

        int n = properties.size();
        unordered_map<int, int> dic;
        for (auto p : properties) {
            if (dic.find(p[0]) != dic.end()) {
                dic[p[0]] = max(dic[p[0]], p[1]);
            } else {
                dic[p[0]] = p[1];
            }
        }

        vector<int> keys;
        // 类似Python的 `.keys()`
        for (auto [k, v] : dic) {
            keys.push_back(k);
        }
        // 倒序排序，类似Python的 `.sort(reverse=True)`
        sort(keys.begin(), keys.end(), greater<int>());
        int m = keys.size();
        // 直接带初始值的字典的申请：语法跟 vector 也不一样，多了一层括号不说，
        // 里面用的是逗号，我还因为 Python 的原因用冒号了。
        unordered_map<int, int> dic2 = {
            {keys[0], dic[keys[0]]}
        };
        for (int i = 1; i < m; ++i) {
            int currKey = keys[i], prevKey = keys[i-1];
            dic2[currKey] = max(dic[prevKey], dic2[prevKey]);
        }

        int maxKey = *max_element(keys.begin(), keys.end());
        sort(properties.begin(), properties.end());
        int res = 0;
        for (int i = 0; i < n - 1; ++i) {
            auto p = properties[i];
            if (p[0] == maxKey) {
                return res;
            }
            if (p[1] < dic2[p[0]]) {
                res += 1;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/263042150/

执行用时：960 ms, 在所有 C++ 提交中击败了5.80%的用户
内存消耗：198.6 MB, 在所有 C++ 提交中击败了5.31%的用户
通过测试用例：
44 / 44
*/
/*
又一个 C++ 版本比 Python 版本还慢的。。。
*/
