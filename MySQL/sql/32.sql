USE madb_n;
SELECT ENAME AS 僱員,
		(SELECT DNAME FROM dept
		WHERE DEPTNO = emp.DEPTNO) AS 部門名稱,
		SAL AS 薪資
        FROM emp