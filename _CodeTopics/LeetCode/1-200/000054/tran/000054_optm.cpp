class Solution {
public:

    vector<int> getOuterElem(vector<vector<int>> mtx, vector<int>& res) {
        int h = mtx.size();
        int w = mtx[0].size();
        if (h == 1) {
            for (int i = 0; i < w; ++i) {
                res.push_back(mtx[0][i]);
            }
            return res;
        }
        if (w == 1) {
            for (int i = 0; i < h; ++i) {
                res.push_back(mtx[i][0]);
            }
            return res;
        }
        for (int i = 0; i < w; ++i) {
            res.push_back(mtx[0][i]);
        }
        for (int i = 1; i < h; ++i) {
            res.push_back(mtx[i][w-1]);
        }
        for (int i = w - 2; i > -1; --i) {
            res.push_back(mtx[h-1][i]);
        }
        for (int i = h - 2; i > 0; --i) {
            res.push_back(mtx[i][0]);
        }
        return res;
    }

    void getInnerMatrix(vector<vector<int>>& mtx) {
        mtx.erase(mtx.begin());
        mtx.pop_back();
        for (auto& row : mtx) {
            row.erase(row.begin());
            /* 
             * 原来 “ERROR: AddressSanitizer: negative-size-param” 这个错就是因为这里误用了：不能删 xxx.end()，
             * 因为末尾的这个index并不存在，所以要删也是用 xxx.end()-1。或者就直接像上面一样用 pop_back()。
             * 之前类似的错应该也是差不多的原因。
             * https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/389931/whats-wrong-with-this-please-help
             */
            // row.erase(row.end());
            row.erase(row.end()-1);
        }
    }

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return {};
        }
        vector<int> res;
        int h = matrix.size();
        int w = matrix[0].size();
        while (h > 1 && w > 1) {
            getOuterElem(matrix, res);
            getInnerMatrix(matrix);
            h -= 2;
            w -= 2;
        }
        if (h == 0 || w ==0) {
            return res;
        } else {
            getOuterElem(matrix, res);
            return res;
        }
    }
};

/*
https://leetcode-cn.com/submissions/detail/155237607/

22 / 22 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 6.7 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.7 MB, 在所有 C++ 提交中击败了66.61%的用户
*/
/*
这次美死了：
- 不但搞了个击败百分之百，而且还是零毫秒（0ms）。
- 最主要还发现了一个之前老疏忽的点：操作迭代器的末尾时候要注意，到底是要操作 xxx.end() 还是 xxx.end() - 1。
*/
