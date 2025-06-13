# MySQL

## 聲明

 本檔案僅紀錄個人操作SQL語言時所見、所聞及所思，內容可能有誤，閱讀過程請抱持謹慎求證的態度

## 基礎指令及邏輯

**Note: SQL *基本上* 並不在乎什麼大小寫**

### *USE*

```sql
USE DATABASE_1;
```

`USE`表示「使用」，DATABASE_1為資料庫名稱。

指令之間以;號區隔

### *SELECT*, *FROM*

```sql
USE DATABASE_1;
SELECT * FROM TABLE_1;
```

此指令的意涵為「使用DATABASE_1資料庫」以及「在資料庫之中尋找 TABLE_1 表」

### *執行順序的邏輯*

在SQL中，指令被執行的順序並不完全是由上而下，由左至右。在以下程式：

```sql
SELECT COL_A, COL_B FROM TABLE_1
WHERE conditions;
```

`SELECT`, `FROM`, `WHERE` 被視為同一個指令，但是他的執行順序並不是：
**`SELECT`→ `FROM` → `WHERE`** 而是，
**`FROM`→ `WHERE`→ `SELECT`**

展開來說，他的順序是：

1. **`FROM` - 找到資料來源**
2. **`WHERE` - 篩選是否符合條件**
3. **`SELECT` - 選擇欄位**

經查詢，完整的順序如下：
**`FROM` → `JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`**

### *WHERE, LIKE, =*

```sql
SELECT * FROM USERS
WHERE USERNAME LIKE '___E' 
    AND U_TYPE LIKE '%NORMAL%'
    AND SHORT_ID > 3 
    AND SEQ_DAY < '2024-08-03';
```

如上面所提，`WHERE`指令會提供條件，在以上這段程式中目標資料的條件是：

1. `USERNAME LIKE '___E'`：這個條件會篩選 USERNAME 欄位中總長度為4個字符，且結尾為 E 的資料，其中`_`表示任意一個字符
2. `U_TYPE LIKE '%NORMAL%'`：這個條件會篩選所有 U_TYPE 欄位中包含 `NORMAL` 的資料，其中`%`表示任意長度字符
3. `SHORT_ID > 3`：這個條件會篩選 SHORT_ID 欄位中數值大於3的資料
4. `SEQ_DAY < '2024-8-3'`：這個條件會篩選 SEQ_DAY 欄位中日期早於2024年8月3號的資料，值得注意的是SQL中自動辨識日期格式的特徵

值得注意的是，根據網路資料，`LIKE`和`=`的功能相仿；但是`=`是相對精確的比較，而`LIKE`則更為模糊，一般而言，對於已知資訊來說使用`=`會是更符合效能的選項，而`LIKE`則適合用於找到「相似」的資料。

### *GROUP BY, ORDER BY*

```sql
SELECT A.PRICE AS 'A PRICE',
    B.PRICE AS 'B PRICE' 
    FROM TABLE_1 AS A,
        TABLE_2 AS B
WHERE A.PRICE IS NOT NULL
    OR B.PRICE IS NOT NULL
GROUP BY A.SHELL
ORDER BY A.PRICE ASC,
    B.PRICE DESC;
```

在這段指令中，根據邏輯順序，會先從`FROM`中找到`TABLE_1`和`TABLE_2`，它們各自被取了一個別名`AS A`和`AS B`，這邊的`AS`是可以省略的。
接著，根據`WHERE`提供的條件，找到`A.PRICE`和`B.PRICE`不為空值(`NULL`)的資料。`NULL`值只能透過邏輯運算`IS`和`NOT`去作運算，不能透過`=`或`!=`或`<>`。
再來，透過`GROUP BY`找到`A`(也就是前面的`TABLE_1`) 表中的`SHELL`欄位進行一次分類，它會將與`A.SHELL`有相同值的資料合併成一組。
接著，程式才會這些指令中`SELECT`出`A`表中的`PRICE`和`B`表中的`PRICE`，並將欄位透過`AS`取別名為`A PRICE`和`B PRICE`。
最後，透過`ORDER BY`指令，對`A.PRICE`進行升序排列，然後再對`B.PRICE`進行降序排列。

### *JOIN*

`JOIN`可謂我學習sql時的一大困擾，使用這個指令時，最主要的問題就是：我想得到它，我也會寫它，但是我其實不太懂它為什麼行？又為什麼會不行？

我最常遇到的一個錯誤訊息就是「ERROR CODE: 1111. Invaild use of group function.」(這則訊息和`GROUP BY`指令有關)

```sql
SELECT FIC.NAME AS 水果,
    FIC.PRICE AS 價格
FROM Fruity_Ice_Cream AS FIC
INNER JOIN Fruity_Member AS FM
    ON FM.MEMBER_NAME = FIC.NAME
    WHERE FM.MEMBER_NAME NOT LIKE '水果奶奶'
    AND FM.MEMBER_DEP = 'CAST'
ORDER BY FIC.PRICE ASC;
```

參考以上範例，這邊使用的`JOIN`指令是`INNER JOIN`，按照`JOIN`指令的邏輯，`INNER`是`JOIN`的類別(稍後會解釋這個類別的特徵)，在`JOIN`之後，我們先引入一個資料`Fruity_Member`並取別名作`FM`，然後在`ON`之後寫入條件：

1. `FM.MEMBER_NAME = FIC.NAME` 使用`ON`確認`FM.MEMBER_NAME`與`FIC.NAME`連結的條件，並比較他們是否在`FIC`(也就是指令前面的`Fruity_Ice_Cream`的別名)表中的`'NAME'`欄之中。
2. `FM.MEMBER_NAME NOT LIKE '水果奶奶'` 表示從`FM`表中取出`MEMBER_NAME`欄的資料，並比較他們是否與'水果奶奶'不同。
3. 再來，從`FM`中找到`MEMBER_DEP`，篩選出內容為`'CAST'`的資料。

在這一串`JOIN`的邏輯中，`INNER`使這一串條件嚴格篩選，引入的表和`FROM`使用的表必須要完全符合條件才會被留下。

根據網路資料：

* `ON`：用於定義表格之間的連接條件
* `WHERE`：用於篩選最終結果

在`JOIN`指令的類別中，除`INNER`還有`FULL`(MySQL不直接支援), `LEFT`, `RIGHT`。
在沒有指示類別的狀況下，單純的`JOIN`會被視為`INNER JOIN`。

### *HAVING*

根據[W3school](https://www.w3schools.com/sql/sql_having.asp)的範例：

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

`HAVING`被用在「你需要新增條件，但是沒辦法寫`WHERE`的地方。」

而網路上有種解釋為：

* `WHERE`：篩選「原始資料列」
* `HAVING`：篩選「分組後的結果」

應避免在`HAVING`中使用複雜運算。
