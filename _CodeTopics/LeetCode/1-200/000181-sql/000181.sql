# Write your MySQL query statement below

SELECT e1.Name AS "Employee"
FROM Employee e1, Employee e2
WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary;

/*
https://leetcode-cn.com/submissions/detail/240071981/

执行用时：384 ms, 在所有 MySQL 提交中击败了70.07%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
通过测试用例：
14 / 14
*/
