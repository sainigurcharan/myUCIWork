--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT
	EMP."EMP_NO",
	EMP."LAST_NAME",
	EMP."FIRST_NAME",
	EMP."GENDER",
	SAL."SALARY"
FROM "EMPLOYEES" as EMP
LEFT JOIN "SALARIES" as SAL
	on (EMP."EMP_NO" = SAL."EMP_NO")

--2. List employees who were hired in 1986.
SELECT
	EMP."EMP_NO", 
	EMP."LAST_NAME", 
	EMP."FIRST_NAME", 
	EMP."GENDER",
	EMP."HIRE_DATE",
	SAL."SALARY"
FROM "EMPLOYEES" as EMP
LEFT JOIN "SALARIES" as SAL
	on (EMP."EMP_NO" = SAL."EMP_NO")
WHERE (EMP."HIRE_DATE" BETWEEN DATE('1986-01-01') AND DATE('1986-12-31'))
ORDER BY EMP."HIRE_DATE" ASC

--3. List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT
	DM."DEPT_NO",
	DP."DEPT_NAME",
	EMP."EMP_NO", 
	EMP."LAST_NAME", 
	EMP."FIRST_NAME", 
	EMP."GENDER",
	DM."FROM_DATE",
	DM."TO_DATE"
FROM "EMPLOYEES" as EMP
JOIN "DEPT_MANAGER" as DM
	on (EMP."EMP_NO" = DM."EMP_NO")
JOIN "DEPARTMENTS" AS DP
	ON (DM."DEPT_NO" = DP."DEPT_NO")

--4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT
	EMP."EMP_NO",
	EMP."LAST_NAME",
	EMP."FIRST_NAME",
	DP."DEPT_NAME"
FROM "EMPLOYEES" as EMP
LEFT JOIN "DEPT_EMP" as DE
	on (EMP."EMP_NO" = DE."EMP_NO")
JOIN "DEPARTMENTS" AS DP
	ON (DE."DEPT_NO" = DP."DEPT_NO")

--5. List all employees whose first name is "Hercules" and last names begin with "B."
SELECT
	"EMP_NO",
	"LAST_NAME",
	"FIRST_NAME"
FROM "EMPLOYEES"
WHERE (UPPER("FIRST_NAME") = 'HERCULES' AND "LAST_NAME" LIKE 'B%')

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT
	EMP."EMP_NO",
	EMP."LAST_NAME",
	EMP."FIRST_NAME",
	DP."DEPT_NAME"
FROM "EMPLOYEES" as EMP
LEFT JOIN "DEPT_EMP" as DE
	on (EMP."EMP_NO" = DE."EMP_NO")
JOIN "DEPARTMENTS" AS DP
	ON (DE."DEPT_NO" = DP."DEPT_NO")
WHERE (UPPER(DP."DEPT_NAME") = 'SALES')

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT
	EMP."EMP_NO",
	EMP."LAST_NAME",
	EMP."FIRST_NAME",
	DP."DEPT_NAME"
FROM "EMPLOYEES" as EMP
LEFT JOIN "DEPT_EMP" as DE
	on (EMP."EMP_NO" = DE."EMP_NO")
JOIN "DEPARTMENTS" AS DP
	ON (DE."DEPT_NO" = DP."DEPT_NO")
WHERE (UPPER(DP."DEPT_NAME") = 'SALES' OR UPPER(DP."DEPT_NAME") = 'DEVELOPMENT')

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT 
	"LAST_NAME",
	COUNT("LAST_NAME") as "LAST_NAME_FREQUENCY"
FROM "EMPLOYEES"
GROUP BY "LAST_NAME"
ORDER BY "LAST_NAME_FREQUENCY" DESC