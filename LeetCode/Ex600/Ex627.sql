# Write your MySQL query statement below
Update Salary
  set Sex = case when Sex = 'm' then 'f'
    when Sex = 'f' then 'm'
    end

# Peer
UPDATE salary SET sex = IF(sex = 'm', 'f', 'm')
