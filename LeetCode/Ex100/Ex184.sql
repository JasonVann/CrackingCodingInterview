# Write your MySQL query statement below
select d.Name as Department, e.Name as Employee, e.Salary
  from Employee e
  inner join (select DepartmentId, max(Salary) as Salary
    from Employee group by DepartmentId) c
    on e.DepartmentId = c.DepartmentId
    and e.Salary = c.Salary
  inner join Department d
    on c.DepartmentId = d.Id

select d.Name as Department, e.Name as Employee, e.Salary
    from Employee e
    inner join Department d
    on e.DepartmentId = d.Id
  where e.Id not in
  (select e.Id from Employee e
    inner join Employee e2
    on e.DepartmentId = e2.DepartmentId
    and e.Salary < e2.Salary)

# Peers
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;

SELECT D.Name AS Department ,E.Name AS Employee ,E.Salary
FROM
	Employee E,
	(SELECT DepartmentId,max(Salary) as max FROM Employee GROUP BY DepartmentId) T,
	Department D
WHERE E.DepartmentId = T.DepartmentId
  AND E.Salary = T.max
  AND E.DepartmentId = D.id

# Faster
SELECT D.Name,A.Name,A.Salary
FROM
	Employee A,
	Department D
WHERE A.DepartmentId = D.Id
  AND NOT EXISTS
  (SELECT 1 FROM Employee B WHERE B.Salary > A.Salary AND A.DepartmentId = B.DepartmentId)
