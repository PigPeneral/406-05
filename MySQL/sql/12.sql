use madb_n;
select EMPNO AS 員工編號, ENAME AS "名字不帶'A'" from emp where ENAME not like '%A%'