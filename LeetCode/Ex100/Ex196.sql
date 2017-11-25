# Write your MySQL query statement below
# Faster
delete from Person
    where Id in
    (select * from (select p.Id from Person p,
      Person p2
      where p.Email = p2.Email
    and p.Id > p2.Id) as p)

# Error: cannot specify target for update in from
delete from Person
    where Id in
    (select p.Id from Person p,
      Person p2
      where p.Email = p2.Email
    and p.Id > p2.Id)

delete Person from Person
  inner join Person p2
  on Person.Email = p2.Email
  and Person.id > p2.id
