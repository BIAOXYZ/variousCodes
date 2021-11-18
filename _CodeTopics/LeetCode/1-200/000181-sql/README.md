
`181. 超过经理收入的员工` https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/solution/chao-guo-jing-li-shou-ru-de-yuan-gong-by-leetcode/
- [x] 方法 1：使用 `WHERE` 语句
- [x] 方法 2：使用 JOIN 语句

# 测试用例

```
{"headers": {"Employee": ["id", "name", "salary", "managerId"]}, "rows": {"Employee": [[1, "Joe", 70000, 3], [2, "Henry", 80000, 4], [3, "Sam", 60000, null], [4, "Max", 90000, null]]}}
```

# 题目

```
SQL架构

Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int)
Truncate table Employee
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3')
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4')
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', 'None')
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', 'None')

Employee 表包含所有员工，他们的经理也属于员工。每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

给定 Employee 表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。在上面的表格中，Joe 是唯一一个收入超过他的经理的员工。

+----------+
| Employee |
+----------+
| Joe      |
+----------+
```
