use madb_n;
select ENAME AS 姓名, EMPNO AS 員工編號, DEPTNO AS 部門名稱 from emp where job not like 'manager' and job not like 'president'