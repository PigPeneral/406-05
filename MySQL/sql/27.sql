USE madb_n;
SELECT DISTINCT CLK.ENAME AS 姓名, CLK.JOB AS 職位, dept.DNAME AS 部門名稱 FROM emp, dept 
INNER JOIN emp AS CLK ON CLK.JOB LIKE 'CLERK'
WHERE dept.DEPTNO = CLK.DEPTNO