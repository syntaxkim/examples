# SQL
2019-01-27

**Lecture from `CS50's Web Programming with Python and JavaScript` by Havard Univercity**
* The example queries are used in `PostgreSQL`.

### CREATE
* Data Types: INTEGER, DECIMAL, SERIAL, VARCHAR, TIMESTAMP, BOOLEAN, ENUM, ...
* Constraints: NOT NULL, UNIQUE, PRIMARY KEY, DEFAULT, CHECK, ...
```
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);
```

### INSERT
```
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
```

### SELECT
#### Basic Usage
```
SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;
```
#### Functions - SUM, COUNT, MIN, MAX, AVG, ...
```
SELECT AVG(duration) FROM flights;
SELECT AVG(duration) FROM flights WHERE origin = 'New York';
SELECT COUNT(*) FROM flights;
SELECT COUNT(*) FROM flights WHERE origin = 'New York';
SELECT MIN(duration) FROM flights;
```
#### IN, LIKE, LIMIT, ORDER BY - ASC/DESC
```
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
SELECT * FROM flights WHERE origin LIKE '%a%';
SELECT * FROM flights LIMIT 2;
SELECT * FROM flights ORDER BY duration ASC;
SELECT * FROM flights ORDER BY duration DESC LIMIT 3;
```
#### GROUP BY, HAVING
```
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
```
#### JOIN
```
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';
SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights RIGHT JOIN passengers ON passengers.flight_id = flights.id;
```
* By default, `JOIN` equals to `INNER JOIN` (Only get the things that match)
* `LEFT JOIN` includes all of the rows in the left table even if they don't have a match.
#### Nested Query.
```
SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1;
SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);
```

### UPDATE
```
UPDATE flights SET duration = 430 WHERE origin = 'New York' AND destination = 'London';
```

### DELETE
```
DELETE FROM flights WHERE destination = 'Tokyo';
```

## Foriegn Key

## CREATE INDEX

## SQL Injection

## Race Condition
### Transaction
* BEGIN, COMMIT