# Write your MySQL query statement below
select s.* from stadium s
  inner join stadium s2
    on s.id < s2.id
    where s.people >= 100
    and s2.people >= 100
  and not exists (select 1 from stadium s3
    where s3.id > s.id and s3.id < s2.id
    and s3.people < 100)


-- Find 1st day
select s1.* from stadium s1
  inner join stadium s2
  on s1.id = s2.id - 1
  and s1.people >= 100
  and s2.people >= 100
  inner join stadium s3
  on s1.id = s3.id-2
  and s3.people >= 100
  and not exists (select 1 from stadium s4 where s4.id = (s1.id-1) and s4.people >= 100)
-- last day
union all
select s1.* from stadium s1
  inner join stadium s2
  on s1.id = s2.id + 1
  and s1.people >= 100
  and s2.people >= 100
  inner join stadium s3
  on s1.id = s3.id+2
  and s3.people >= 100
  and not exists (select 1 from stadium s4 where s4.id = (s1.id+1) and s4.people >= 100)
-- middle
union all
select s1.* from stadium s1
  inner join stadium s2
  on s1.id = s2.id - 1
  and s1.people >= 100
  and s2.people >= 100
  inner join stadium s3
  on s1.id = s3.id+1
  and s3.people >= 100
  -- and exists (select 1 from stadium s4 where s4.id = (s1.id-1) and s4.people >= 100)
order by date

# Peer
SELECT s1.* FROM stadium AS s1, stadium AS s2, stadium as s3
    WHERE
    ((s1.id + 1 = s2.id
    AND s1.id + 2 = s3.id)
    OR
    (s1.id - 1 = s2.id
    AND s1.id + 1 = s3.id)
    OR
    (s1.id - 2 = s2.id
    AND s1.id - 1 = s3.id)
    )
    AND s1.people>=100
    AND s2.people>=100
    AND s3.people>=100
    GROUP BY s1.id

SELECT t.* FROM stadium t
        LEFT JOIN stadium p1 ON t.id - 1 = p1.id
        LEFT JOIN stadium p2 ON t.id - 2 = p2.id
        LEFT JOIN stadium n1 ON t.id + 1 = n1.id
        LEFT JOIN stadium n2 ON t.id + 2 = n2.id
    WHERE (t.people >= 100 AND p1.people >= 100 AND p2.people >= 100)
         OR (t.people >= 100 AND n1.people >= 100 AND n2.people >= 100)
         OR (t.people >= 100 AND n1.people >= 100 AND p1.people >= 100)
    ORDER BY id;

SELECT
      *
    FROM
      stadium
    WHERE INSTR(
        (SELECT CONCAT(',',GROUP_CONCAT(tmpaa.ids),',') AS ids FROM (SELECT
          GROUP_CONCAT(id) AS ids
        FROM
          (SELECT
            id,
            CASE
              WHEN (
                (@prevone := people) < 100
                OR (@prevone >= 100
                  AND @prevtwo < 100)
              )
              THEN @group := @group + 1
              ELSE @group := @group
            END AS groupno,
            (@prevtwo := people) AS bb
          FROM
            stadium,
            (SELECT
              @group := 0,
              @prevone := - 1,
              @prevtwo := - 1) init) AS tmp
        GROUP BY tmp.groupno
        HAVING COUNT(1) >= 3 ) AS tmpaa),
        CONCAT(',', id, ',')
      ) > 0
