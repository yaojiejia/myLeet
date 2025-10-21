-- Write your PostgreSQL query statement below
with low as (select 'Low Salary' as category, sum(case when a.income < 20000 then 1 else 0 end) as "accounts_count" 
from Accounts a), avg as (
    select 'Average Salary' as category, sum(case when a.income <= 50000 and a.income >= 20000 then 1 else 0 end) as "accounts_count" 
from Accounts a
),
high as (
    select 'High Salary' as category, sum(case when a.income > 50000 then 1 else 0 end) as "accounts_count" 
from Accounts a
)


select * from low
union
select * from avg
union
select * from high