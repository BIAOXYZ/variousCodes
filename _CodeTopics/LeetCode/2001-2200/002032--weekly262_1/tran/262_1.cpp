class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {

        // 第 262 场周赛第一题
        // https://leetcode.cn/submissions/detail/227322774/

        unordered_map<int, int> dic;
        unordered_set<int> res;
        for (auto& arr_vec : {nums1, nums2, nums3}) {
            unordered_set<int> arr(arr_vec.begin(), arr_vec.end());
            for (auto elem : arr) {
                if (dic.find(elem) != dic.end()) {
                    dic[elem]++;
                } else {
                    dic[elem] = 1;
                }
                if (dic[elem] >= 2) {
                    res.insert(elem);
                }
            }
        }
        return vector<int>(res.begin(), res.end());
    }
};

/*
https://leetcode.cn/submissions/detail/391623757/

执行用时：
28 ms
, 在所有 C++ 提交中击败了
11.57%
的用户
内存消耗：
27.8 MB
, 在所有 C++ 提交中击败了
8.79%
的用户
通过测试用例：
288 / 288
*/
