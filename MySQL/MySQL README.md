# MySQL

---

## 聲明

 本檔案僅紀錄個人操作SQL語言時所見、所聞及所思，內容可能有誤，閱讀過程請抱持謹慎求證的態度

---

## 基礎指令及邏輯

**Note: SQL *基本上* 並不在乎什麼大小寫**

1. ***USE***

```sql
USE DATABASE_1;
```

USE表示「使用」，DATABASE_1為資料庫名稱。

指令之間以;號區隔

2. ***SELECT***, ***FROM***

```sql
USE DATABASE_1;
SELECT * FROM TABLE_1;
```

此指令的意涵為「使用DATABASE_1資料庫」以及「在資料庫之中尋找 TABLE_1 表」

3. ***執行順序的邏輯***

在SQL中，指令被執行的順序並不完全是由上而下，由左至右。在以下程式：

```sql
SELECT COL_A, COL_B FROM TABLE_1
WHERE conditions;
```

SELECT, FROM, WHERE 被視為同一個指令，但是他的執行順序並不是：
**SELECT→ FROM → WHERE** 而是，
**FROM→ WHERE→ SELECT**

展開來說，他的順序是：

1. **FROM - 找到資料來源**
2. **WHERE - *篩選是否符合條件***
3. **SELECT - 選擇欄位**

經查詢，完整的順序如下：
**FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT**

- 待續
