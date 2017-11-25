# Write your MySQL query statement below
select a.Name as 'Employee' from Employee a
  inner join Employee b
    on a.ManagerId = b.Id
    and a.Salary > b.Salary

-- Peer
SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary
;
