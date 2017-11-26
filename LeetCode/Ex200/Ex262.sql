select distinct(Day), ROUND(A/B, 2) as 'Cancellation Rate'
from (
  select Request_at as 'Day', (select count(*) from Trips T1
                            inner join Users U
                               on T1.Client_Id = U.Users_Id
    where T.Request_at = T1.Request_at and Banned = 'No' and Status <> 'Completed') A,
    (select count(*) from Trips T2
        inner join Users U
                               on T2.Client_Id = U.Users_Id
    where T.Request_at = T2.Request_at and Banned = 'No') B
    from Trips T
    where Request_at between '2013-10-01' and '2013-10-03') B

# Peer
select
  t.Request_at Day,
  round(sum(case when t.Status like 'cancelled_%' then 1 else 0 end)/count(*),2) Rate
  from Trips t
  inner join Users u
  on t.Client_Id = u.Users_Id and u.Banned='No'
  where t.Request_at between '2013-10-01' and '2013-10-03'
  group by t.Request_at

select Day, round(avg(cnt), 2) as "Cancellation Rate"
  from
  (   select a.request_at as Day,
      @cnt := IF(a.Status = 'completed', 0, 1) as cnt
      from Trips a, Users b
      where a.Client_Id = b.Users_Id and b.Banned = 'No'
  ) c
  where Day BETWEEN '2013-10-01' AND '2013-10-03'
  group by Day
