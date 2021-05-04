
SELECT * FROM employee;

SELECT DISTINCT empName FROM employee;

SELECT empName FROM employee
WHERE deptId = 1;

SELECT * FROM employee
GROUP BY deptId
HAVING deptId in (1, 2, 3);