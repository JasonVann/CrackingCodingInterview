# Write your MySQL query statement below
select P.FirstName, P.LastName, A.City, A.State from Address A
    right join Person P
        on A.PersonId = P.PersonId
