# Write your MySQL query statement below
select w.Id from Weather w
  inner join Weather w2
    on datediff(w.date, w2.date) = 1
    and w.temperature > w2.temperature

# Peer
# Faster
SELECT Id FROM (
    SELECT CASE
        WHEN Temperature > @prevtemp AND DATEDIFF(Date, @prevdate) = 1 THEN Id ELSE NULL END AS Id,
        @prevtemp:=Temperature,
        @prevdate:=Date
    FROM Weather, (SELECT @prevtemp:=NULL) AS A, (SELECT @prevdate:=NULL) AS B ORDER BY Date ASC
) AS D WHERE Id IS NOT NULL
