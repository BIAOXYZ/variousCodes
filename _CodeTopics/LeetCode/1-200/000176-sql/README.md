
`176. 第二高的薪水` https://leetcode-cn.com/problems/second-highest-salary/solution/di-er-gao-de-xin-shui-by-leetcode/
- [x] 方法一：使用子查询和 `LIMIT` 子句
- [x] 方法二：使用 `IFNULL` 和 `LIMIT` 子句

# 测试用例

```
{"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100],[2,200],[3,300]]}}

{"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100]]}}
```

# 题目

```
SQL架构

Create table If Not Exists Employee (id int, salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

# SQL语法点

SQL - Distinct Keyword https://www.tutorialspoint.com/sql/sql-distinct-keyword.htm

SQL LIMIT https://www.sqltutorial.org/sql-limit/
- > The `OFFSET` clause is optional. If you omit it, the query will return the "row_count" rows from the first row returned by the `SELECT` clause.

MySQL ifnull()函数 https://www.yiibai.com/mysql/ifnull.html
