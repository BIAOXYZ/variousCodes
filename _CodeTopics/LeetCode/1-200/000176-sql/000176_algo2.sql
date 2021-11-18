# Write your MySQL query statement below

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;

/*
https://leetcode-cn.com/submissions/detail/240071210/

执行用时：212 ms, 在所有 MySQL 提交中击败了57.39%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
通过测试用例：
7 / 7
*/
