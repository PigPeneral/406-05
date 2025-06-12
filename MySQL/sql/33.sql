USE madb_n;
SELECT DEPTNO AS 部門編號,
	DNAME AS 部門名稱,
    LOC AS 區域,
    (SELECT count(*) FROM emp WHERE DEPTNO=dept.DEPTNO) AS 人數
    FROM dept