USE madb_n;	
SELECT dept.DEPTNO AS 部門編號, dept.DNAME AS 部門名稱, COUNT(emp.ENAME) AS 人數 FROM emp, dept WHERE emp.DEPTNO = 10 AND dept.DEPTNO = 10
union
SELECT dept.DEPTNO AS 部門編號, dept.DNAME AS 部門名稱, COUNT(emp.ENAME) AS 人數 FROM emp, dept WHERE emp.DEPTNO = 20 AND dept.DEPTNO = 20 
union
SELECT dept.DEPTNO AS 部門編號, dept.DNAME AS 部門名稱, COUNT(emp.ENAME) AS 人數 FROM emp, dept WHERE emp.DEPTNO = 30 AND dept.DEPTNO = 30;

-- 參考解法
--  select D.DeptNO , DNAME  , E.
-- 	from  Dept D 
-- 	inner join (select DEPTNO,Count(*) 人數 from Emp  Group by DEPTNO ) E
--  on D.DEPTNO=E.DEPTNO;