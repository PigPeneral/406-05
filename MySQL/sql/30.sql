USE madb_n;
SELECT DISTINCT E.ENAME AS 僱員, E.SAL AS 薪資 FROM emp AS E
INNER JOIN (
	SELECT ENAME, SAL FROM emp
    WHERE DEPTNO = 30) AS E30 ON
    E.SAL = E30.SAL