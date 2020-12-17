// 主要是为了修正 `deliberate-WA--000217_algo1.c`
//
// https://troydhanson.github.io/uthash/userguide.html
// 参见上面链接中 “Passing the hash pointer into functions” 这一小节，
// 解释了为啥用子函数的形式往哈希表里添加元素时如此麻烦（因为涉及到二级指针）。。。

struct htElement {
    int key;
    int val;
    UT_hash_handle hh;
};

void add_elem(struct htElement** dic, int k, int v) {
    struct htElement* kvPair;
    kvPair = malloc(sizeof(struct htElement));
    kvPair->key = k;
    kvPair->val = v;
    HASH_ADD_INT(*dic, key, kvPair);
}
struct htElement *find_elem(struct htElement* dic, int* ptr_to_k) {
    struct htElement *kvPair;
    HASH_FIND_INT(dic, ptr_to_k, kvPair);
    return kvPair;
}

bool containsDuplicate(int* nums, int numsSize){
    struct htElement* dic = NULL;
    for (int i = 0; i < numsSize; i++) {
        struct htElement *kvPair = find_elem(dic, nums + i);
        if (kvPair == NULL) {
            add_elem(&dic, nums[i], i);
        }
        else {
            return true;
        }
    }
    return false;
}

/*
https://leetcode-cn.com/submissions/detail/131762973/

18 / 18 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 16.3 MB

执行用时：44 ms, 在所有 C 提交中击败了20.68%的用户
内存消耗：16.3 MB, 在所有 C 提交中击败了6.53%的用户
*/
