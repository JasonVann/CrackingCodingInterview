# Write your MySQL query statement below
select a.Email
  from Person a
  group by Email
  having count(*) > 1

# 50% faster
select distinct a.Email
  from Person a
  inner join Person b
  on a.Email = b.Email
  and a.Id != b.Id
