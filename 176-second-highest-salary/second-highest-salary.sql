# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
FROM employee
where salary not in (select max(salary) from employee)