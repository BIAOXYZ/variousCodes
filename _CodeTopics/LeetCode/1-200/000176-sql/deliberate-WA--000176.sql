# Write your MySQL query statement below

SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1

/*
https://leetcode-cn.com/submissions/detail/240070555/

5 / 7 个通过测试用例
状态：解答错误

输入：
{"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100]]}}
输出：
{"headers": ["SecondHighestSalary"], "values": []}
预期结果：
{"headers":["SecondHighestSalary"],"values":[[null]]}
*/
