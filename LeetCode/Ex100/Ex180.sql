# Write your MySQL query statement below
select distinct a.Num from Logs a
	inner join Logs b
		on a.ID = b.ID + 1
	inner join Logs c
		on a.ID = c.ID + 2
	where a.NUm = b.Num
		and a.Num = c.Num;

-- Faster
select distinct Num as ConsecutiveNums
    from (select a.Num from Logs a
            inner join Logs b
                on a.Id = b.Id - 1
                and a.Num = b.Num
            inner join Logs c
                on b.Id = c.Id - 1
                and b.Num = c.Num) as d

-- Peers
Select DISTINCT l1.Num from Logs l1, Logs l2, Logs l3
where l1.Id=l2.Id-1 and l2.Id=l3.Id-1
and l1.Num=l2.Num and l2.Num=l3.Num
