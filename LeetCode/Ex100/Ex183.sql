# Write your MySQL query statement below
select a.Name as Customers
  from Customers a
  left join Orders b
    on a.Id = b.CustomerId
  where CustomerId is null

# Peer
# Faster
select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);

SELECT A.Name from Customers A
WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId)
