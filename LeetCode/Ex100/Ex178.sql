# Write your MySQL query statement below
select t.Score, t.Rank from
  (select Score, @Rank := (CASE
      WHEN @PrevScore = s.Score then @Rank
      ELSE @Rank + 1 END) as Rank,
      @PrevScore := s.Score
    from Scores s, (SELECT @Rank := 0, @PrevScore := 0) r
    order by Score desc) t order by Rank asc

# Peer
SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) Rank
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc

select Score,
  case
    when @prevScore = Score then @rank
    when (@prevScore := Score) is not null then @rank := @rank+1
  end as Rank
from Scores, (select @rank := 0, @prevScore := NULL) a
order by Score desc;

SELECT
  Score,
  (SELECT count(distinct Score) FROM Scores WHERE Score >= s.Score) Rank
FROM Scores s
ORDER BY Score desc

SELECT
  Score,
  (SELECT count(*) FROM (SELECT distinct Score s FROM Scores) tmp WHERE s >= Score) Rank
FROM Scores
ORDER BY Score desc

SELECT s.Score, count(distinct t.score) Rank
FROM Scores s JOIN Scores t ON s.Score <= t.score
GROUP BY s.Id
ORDER BY s.Score desc

SELECT T2.Score Score,
      (SELECT COUNT(*) + 1
      FROM (SELECT T1.Score FROM Scores T1
        GROUP BY Score ORDER BY Score DESC) TEMP
      WHERE T2.Score < TEMP.Score) Rank
    FROM Scores T2 ORDER BY Score DESC;

SELECT Scores.Score, Q3.Rank
    FROM(
        SELECT Q1.Score as Score, COUNT(Q1.Score) as Rank
        FROM
            (SELECT DISTINCT Score from Scores) as Q1,
            (SELECT DISTINCT Score from Scores) as Q2
        WHERE Q1.Score <= Q2.Score
        GROUP BY Q1.Score
        ) as Q3, Scores
    WHERE Q3.Score = Scores.Score
    ORDER BY Scores.Score DESC
