-- Write your PostgreSQL query statement below
with dis as (select distinct e.salary, d.name,
dense_rank() over(partition by d.name order by e.salary desc) as rnk
from Employee e
join Department d
on e.departmentId = d.id)

-- select * from dis where dis.rnk <= 3
select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e
join Department d
on e.departmentId  = d.id
where ((d.name,e.salary) in (select a.name,a.salary from dis a where a.rnk <= 3))
