class Solution {
public:
    int findLHS(vector<int>& nums) {

        // https://leetcode-cn.com/submissions/detail/240558974/

        std::function vec_to_umap = [](vector<int>& vec) -> unordered_map<int, int> {
            unordered_map<int, int> umap = {};
            for (int elem : vec) {
                if (umap.find(elem) != umap.end()) {
                    umap[elem] += 1;
                } else {
                    umap[elem] = 1;
                }
            }
            return umap;
        };

        unordered_map<int, int> dic = vec_to_umap(nums);
        int res = 0;
        for (auto [k, v] : dic) {
            if (dic.find(k+1) != dic.end()){
                res = max(res, v + dic[k+1]);
            }
            if (dic.find(k-1) != dic.end()){
                res = max(res, v + dic[k-1]);
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/240637106/

执行用时：68 ms, 在所有 C++ 提交中击败了73.83%的用户
内存消耗：38.9 MB, 在所有 C++ 提交中击败了79.15%的用户
通过测试用例：
206 / 206
*/
