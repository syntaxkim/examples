# MySQL Tutorial
2019-01-29

[Reference](https://dev.mysql.com/doc/refman/8.0/en/tutorial.html)1

## Connecting to and Disconnecting from the Server
shell> mysql -h host -u user -p
* You can omit `-h host` if you're on the same machine.
mysql> quit or \q

## Entering Queries
mysql> SELECT VERSION(), CURRENT_DATE;
```
+-----------+--------------+
| version() | current_date |
+-----------+--------------+
| 8.0.14    | 2019-01-29   |
+-----------+--------------+
1 row in set (0.00 sec)
```
* The execution time is imprecise as they represent wall clock time.
* Keywords may be entered in any lettercase: `version()` = `vErSiOn()`
* Multiple statements are possible: `SELECT VERSION(); SELECT NOW();`
* Cancel query by typing `\c`.
* '>, "> prompts indicate that you're missing quote(s) to end the string.

## Creating and Using a Database
mysql> SHOW DATABASES;
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.02 sec)
```
mysql> USE database
* No need to use semicolon with `USE`
mysql> GRANT ALL ON database.* TO 'your_mysql_name'@'your_client_host';

### Creating and Selecting a Database
mysql> CREATE DATABASE menagerie;
mysql> USE menagerie
shell> mysql -h host -u user -p menagerie
* While not recommended, you can specify password with no space as `-ppassword`
* To check the selected database, `SELECT DATABASE();`

### Creating a Table
mysql> SHOW TABLES;
mysql> CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),
       species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
mysql> DESCRIBE pet;
* For more information about MySQL data types, [Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

### Loading Data into a Table
mysql> INSERT INTO pet
       VALUES ('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', NULL);
* `LOAD DATA` statement can insert multiple records at once by loading `txt` file.

### Retriveing Information from a Table

#### Selecting All Data
mysql> SELECT * FROM `table`;

#### Selecting Particular Data
mysql> SELECT `columns` FROM `table` WHERE `conditions`;
mysql> UPDATE `table` SET `column`=`value` WHERE `conditions`;
* Intermixed `conditions`: (`condition`) AND/OR (`condition`)
mysql> SELECT DISTINCT `column` FROM `table`;
* `DISTINCT` removes duplicated results.

#### Sorting Rows
mysql> SELECT `columns` FROM `table` ORDER BY `columns`;
mysql> SELECT `columns` FROM `table` ORDER BY `columns` DESC;
* `DESC` only applies to the name immediately preceding it.

#### Date Calculations
mysql> SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age FROM pet;
```
+----------+------------+------------+------+
| name     | birth      | CURDATE()  | age  |
+----------+------------+------------+------+
| Puffball | 1999-03-30 | 2019-01-29 |   19 |
| Fluffy   | 1993-02-04 | 2019-01-29 |   25 |
| Claws    | 1994-03-17 | 2019-01-29 |   24 |
| Buffy    | 1989-05-13 | 2019-01-29 |   29 |
| Fang     | 1990-08-27 | 2019-01-29 |   28 |
| Bower    | 1979-08-31 | 2019-01-29 |   39 |
| Chirpy   | 1998-09-11 | 2019-01-29 |   20 |
+----------+------------+------------+------+
```
* `TIMESTAMPDIFF()` function takes three arguments(the unit of the result, date, date)
* To sort the output, use `ORDER BY` clause.
mysql> SELECT name, birth, death,
       TIMESTAMPDIFF(YEAR,birth,death) AS age
       FROM pet WHERE death IS NOT NULL ORDER BY age;
```
+-------+------------+------------+------+
| name  | birth      | death      | age  |
+-------+------------+------------+------+
| Bower | 1979-08-31 | 1995-07-29 |   15 |
+-------+------------+------------+------+
```
mysql> SELECT name, birth FROM pet WHERE MONTH(birth) = 5;
mysql> SELECT MONTH(CURDATE());
mysql> SELECT MOD(MONTH(CURDATE()), 12) + 1;
* `MOD(MONTH(CURDATE()), 12) + 1` equals to the next month.

#### Working with NULL Values
* Conceptually, `NULL` means *a missing unknown value*
* `IS NULL` or `IS NOT NULL` can be used to test for `NULL`
* In MySQL, `0` or `NULL` means false and anything else means true.
* `0` or empty string are `NOT NULL`.

#### Pattern Matching
mysql> SELECT * FROM pet WHERE name LIKE 'b%';
mysql> SELECT * FROM pet WHERE name LIKE '_____';
* `%`: an arbitrary number of characters.
* `_`: a single character / `_____`: five characters
mysql> SELECT * FROM pet WHERE REGEXP_LIKE(name, '^b');
* `REGEXP_LIKE()` function uses regular expressions.

#### Counting Rows
mysql> SELECT COUNT(*) FROM pet;
mysql> SELECT owner, COUNT(*) FROM pet GROUP BY owner;
```
+--------+----------+
| owner  | count(*) |
+--------+----------+
| Diane  |        2 |
| Harold |        2 |
| Gwen   |        2 |
| Benny  |        1 |
+--------+----------+
```
mysql> SELECT species, COUNT(*) FROM pet
       WHERE species = 'dog' OR species = 'cat'
       GROUP BY species;

#### Using More Than one Table
mysql> CREATE TABLE event (name VARCHAR(20), date DATE,
       type VARCHAR(15), remark VARCHAR(255));
mysql> INSERT INTO event VALUES
       ('Fluffy', '1995-05-15', 'litter', '4 kittens, 3 female, 1 male');
mysql> SELECT pet.name FROM pet INNER JOIN event ON pet.name = event.name;
```
+--------+
| name   |
+--------+
| Fluffy |
+--------+
```
* `INNER JOIN`: only if both tables matche `ON` clause
* You can use `JOIN` with the same table as well.

### Getting Information About Databases and Tables
mysql> SELECT DATABASE();
* The result is `NULL` if you have not selected any.
mysql> SHOW TABLES;
mysql> DESCRIBE pet;
* `DESC` is a short form of `DESCRIBE`.
mysql> SHOW CREATE TABLE pet;
mysql> SHOW INDEX FROM pet;
