# Write your MySQL query statement below
# Extra Select to hand [] as null
select (select * from (select E.Salary
    from Employee E
    where (select count(*) from Employee b where b.Salary > E.Salary) = 1
        ) as c limit 1) as 'SecondHighestSalary'

select (select Salary from
  Employee where Salary not in
    (select * from (select Salary from Employee
      order by Salary desc limit 1) as T )
  order by Salary desc limit 1)
as 'SecondHighestSalary'

# Peer
select (
  select distinct Salary from Employee order by Salary Desc limit 1 offset 1
)as second

SELECT distinct(Salary) FROM Employee
UNION
SELECT NULL
ORDER BY Salary DESC LIMIT 1,1

select case
when count(Salary) > 1 then (select distinct Salary from Employee
    order by Salary DESC limit 1, 1)
else NULL end
from Employee;

# Write your MySQL query statement below
select max(Salary) as 'SecondHighestSalary' from Employee
  where Salary not in (select max(Salary) from Employee)
