# Write your MySQL query statement below
select * from cinema
  where id % 2 <> 0
    and description <> 'boring'
  order by rating desc

# Peer
select *
from cinema
where mod(id, 2) = 1 and description != 'boring'
order by rating DESC
;

SELECT * FROM cinema
  WHERE (id & 1) AND (CHAR_LENGTH(description) <> 6 OR description <> "boring")
  ORDER by rating DESC;
