CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE M INT;
    SET M = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary from Employee
        order by Salary desc limit M, 1
  );
END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE M INT;
    SET M = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary from Employee
        order by Salary desc limit 1 offset M
  );
END

# Peer
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

RETURN (
  # Write your MySQL query statement below.
  
  SELECT e1.Salary
  FROM (SELECT DISTINCT Salary FROM Employee) e1
  WHERE (SELECT COUNT(*) FROM (SELECT DISTINCT Salary FROM Employee) e2 WHERE e2.Salary > e1.Salary) = N - 1

  LIMIT 1

);
END
