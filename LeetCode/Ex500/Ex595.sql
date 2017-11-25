# Write your MySQL query statement below
select name, population, area
  from world
  where area > 3000000 or population > 25000000

# Peer
# May be faster as it can use different index in separate scans of columns
SELECT
    name, population, area
FROM
    world
WHERE
    area > 3000000

UNION

SELECT
    name, population, area
FROM
    world
WHERE
    population > 25000000
;
