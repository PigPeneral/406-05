USE madb_n;
SELECT dept.DEPTNO AS 部門編號, 
       dept.DNAME AS 部門名稱, 
       dept.LOC AS 區域,
       (SELECT COUNT(*) FROM emp WHERE emp.DEPTNO = dept.DEPTNO) AS 人數
FROM dept;