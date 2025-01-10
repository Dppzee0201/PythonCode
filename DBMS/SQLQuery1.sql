

select min(salary) from Employee;

select max(salary) from Employee;

select max(emp_name) from Employee;

select sum(emp_id) from Employee;

select avg(salary) from Employee;

select count(emp_id) from Employee;

select count(*) from Employee;

select distinct(dept) from Employee

select * from Employee

select count(distinct(dept)) from Employee

select count(dept) from Employee

select top  3 * from Employee

select * from Employee

select dept,min(salary)
from Employee 
where salary is not null
group by dept

select dept,min(salary)
from Employee 
group by dept

select dept,count(*) 
from Employee
group by dept

select * from Employee

------