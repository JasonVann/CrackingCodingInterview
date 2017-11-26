select d.Name as 'Department', e.Name as 'Employee', Salary
  from Employee e
  inner join Department d
  on e.DepartmentId = d.Id
  where  (select count(distinct e2.Salary)
    from
  Employee e2
  where e.DepartmentId = e2.DepartmentId
  and e2.Salary > e.Salary)
  < 3

# Peer
SELECT d.Name AS Department, se.Name AS Employee, se.Salary
FROM Department d,
 ( SELECT e.Name, e.DepartmentId, e.Salary,
          @Rank := (CASE
					WHEN @PrevDept != e.DepartmentId THEN 1
                    WHEN @PrevSalary = e.Salary THEN @Rank
					ELSE @Rank + 1 END) AS Rank,
		  @PrevDept := e.DepartmentId,
          @PrevSalary := e.Salary
	FROM Employee e, (SELECT @Rank := 0, @PrevDept := 0, @PrevSalary := 0) r
	ORDER BY DepartmentId ASC, Salary DESC
  ) se
WHERE d.Id = se.DepartmentId AND se.Rank <= 3

select d.Name as Department, e.Name as Employee, computed.Salary as Salary
from Employee e,
	(
		select Salary, DepartmentId, @row := IF(DepartmentId=@did, @row + 1,1) as Rank ,
      @did:=DepartmentId
		from (
			select distinct Salary, DepartmentId
			from Employee
			order by DepartmentId, Salary desc
			) ordered, (select @row:=0, @did:=0) variables
	) computed,
	Department d
where e.Salary=computed.Salary
and e.DepartmentId=computed.DepartmentId
and computed.DepartmentId=d.Id
and computed.Rank<=3
order by computed.DepartmentId, Salary desc

select D.Name as Department, E.Name as Employee, E.Salary as Salary
  from Employee E, Department D
   where (select count(distinct(Salary)) from Employee
           where DepartmentId = E.DepartmentId and Salary > E.Salary) in (0, 1, 2)
         and
           E.DepartmentId = D.Id
         order by E.DepartmentId, E.Salary DESC;

select d.Name, r.Name, r.Salary
from (
  select DepartmentId, Name, Salary,(
    select count(*)+1 from (
      select distinct salary, DepartmentId from Employee
      ) as uniq
     where DepartmentId = e.DepartmentId and Salary > e.Salary
    ) as rank
  from Employee e
  ) as r, Department d
where r.DepartmentId = d.Id and r.rank <= 3
