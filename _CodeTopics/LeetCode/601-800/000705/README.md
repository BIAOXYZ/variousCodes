
`705. 设计哈希集合` https://leetcode-cn.com/problems/design-hashset/solution/she-ji-ha-xi-ji-he-by-leetcode-solution-xp4t/
- [x] 方法一：链地址法

# 测试用例

```
["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
[[],[1],[2],[1],[3],[2],[2],[2],[2]]
["MyHashSet","add","remove","add","remove","remove","add","add","add","add","remove"]
[[],[9],[19],[14],[19],[9],[0],[3],[4],[0],[9]]
```

# 语法点

## C++ STL里的`set`数据结构。

std::set http://www.cplusplus.com/reference/set/set/
- std::set::find http://www.cplusplus.com/reference/set/set/find/
  * `std::set<int>::iterator it;`

[:star:][`*`]】C++中set用法详解 https://www.cnblogs.com/wkfvawl/p/11041079.html
- > （2）为何每次insert之后，以前保存的iterator不会失效？
  * > iterator这里就相当于指向节点的指针，内存没有变，指向内存的指针怎么会失效呢(当然被删除的那个元素本身已经失效了)。相对于vector来说，每一次删除和插入，指针都有可能失效，调用push_back在尾部插入也是如此。因为为了保证内部数据的连续存放，iterator指向的那块内存在删除和插入过程中可能已经被其他内存覆盖或者内存已经被释放了。即使时push_back的时候，容器内部空间可能不够，需要一块新的更大的内存，只有把以前的内存释放，申请新的更大的内存，复制已有的数据元素到新的内存，最后把需要插入的元素放到最后，那么以前的内存指针自然就不可用了。特别时在和find等算法在一起使用的时候，牢记这个原则：不要使用过期的iterator。
- > find
  * > find()，返回给定值的定位器，如果没找到则返回end()。

## C++ 二维数组/二维向量初始化

C++-二维vector初始化大小方法-备忘 https://www.cnblogs.com/ZERO-/p/9736482.html
- > 1.直接用初始化方法。名字为vec，大小为n*m，初始值为0的二维vector。
  ```cpp
  vector<vector<int> > vec(n, vector<int>(m, 0));
  ```
- > 2.用resize()来控制大小
  ```cpp
  vector<vector<int> > vec;
      vec.resize(n);//n行
      for (int i = 0; i < n; ++i){
          vec[i].resize(m);//每行为m列
      }
  ```

## C++ 类成员变量初始化时，编译器可能区分不出是`成员变量`还是`成员函数`

C++编译报错：error: expected parameter declarator vector＜int＞ a(31,-1)； https://haihong.blog.csdn.net/article/details/109478159
- > 针对error: expected parameter declarator这一错误，有三种解决方法：[在C++类中vector声明，报错 “expected parameter declarator”](https://blog.csdn.net/m0_47696151/article/details/107367876)
  * 在C++类中vector声明，报错 “expected parameter declarator” https://blog.csdn.net/m0_47696151/article/details/107367876
