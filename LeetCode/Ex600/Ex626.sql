# Write your MySQL query statement below
select s.id, s2.student
  from seat s
  inner join seat s2
    on s.id & 1
    and s2.id = s.id+1
  union
  select s2.id, s.student
    from seat s
    inner join seat s2
      on s.id & 1
      and s2.id = s.id+1
union
select id, student
    from seat
    where id & 1
    and not exists (select 1 from seat s2 where s2.id > seat.id)
    order by id

# Peer
select
if(id < (select count(*) from seat), if(id mod 2=0, id-1, id+1), if(id mod 2=0, id-1, id)) as id, student
from seat
order by id asc;

select s1.id,
case when mod(s1.id, 2)=1 then
    case when s2.student is null then s1.student else s2.student end
    else s3.student end as student
from seat s1
left join seat s2
on s1.id=s2.id-1
left join seat s3
on s1.id=s3.id+1
order by s1.id asc

SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS counts
    FROM
        seat) AS seat_counts
ORDER BY id ASC;

SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;

/* get all the even numbered rows as odd numbered rows */
SELECT s1.id - 1 as id, s1.student
FROM Seat s1
WHERE s1.id MOD 2 = 0

UNION

/* get all the odd numbered rows as even numbered rows */
SELECT s2.id + 1 as id, s2.student
FROM Seat s2
WHERE s2.id MOD 2 = 1 AND s2.id != (SELECT MAX(id) FROM Seat)
/* Just don't get the last row as we will handle it in the next UNION */

UNION

/* get the last row if odd and don't change the id value */
SELECT s3.id, s3.student
FROM Seat s3
WHERE s3.id MOD 2 = 1 AND s3.id = (SELECT MAX(id) FROM Seat)

/* Order the result by id */
ORDER BY id ASC;
