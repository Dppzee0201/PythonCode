select * from Employee;

--1.Display employees having salary is equal to 7000
select * from Employee where salary=75000;

--2.Display employees having salary less than 2400 and hiring year greater than 2005.
select * from Employee where salary < 400000 and hiring_year > 2005

--3.Display all employees in IT or Accounting department.
select emp_name from Employee where dept='IT' or dept='MBBS'

--4.How to display employees whose salary between 1500 and 2500 without using between operators?
select salary from Employee where salary > 75000 and salary < 455000

--5.Delete employees from department Purchasing and salary less than 2500.
delete Employee where dept='IT' and salary > 90000

--6.Display first name last name and salary of an employee who is having max salary.
select emp_name,salary from Employee where salary=(select max(salary) from Employee)

--Display First_name which not starting with vowels.
select * from Employee where  
emp_name not like 'a%' and 
emp_name not like 'e%' and 
emp_name not like 'o%' and 
emp_name not like 'u%' and
emp_name not like 'i%';

--Q1.Find the total number of streams by date.
select count(date) from table2

--Q.2 Find the total number of streams by date and director.
