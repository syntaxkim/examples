# Scalability
2019-01-16

**Lecture 10 from CS50's Web Programming with Python and JavaScript by Havard University**

## Scaling Servers
* Benchmarking - Load Test, Stress Test
### Vertical Scaling
* Upgrade servers.
### Horizontal Scaling
* Add more servers.
* Load Balancer: Route traffic to servers.
* Load Balancing Methods - Random Choice, Round Robin, Fewest Connections, ...
* Session-Aware Load Balancing - Sticky Sessions(Cookies), Sessions in Database, Client-Side Sessions(Cookies), ...
Flask by default uses a private key and a signed cookie which includes session information. (Sticky Sessions))
### Autoscaling
* Cloud Computing Services - AWS, Microsoft Azure, ...
* Heartbeat Signal: Servers can let a load balancer know which is running or not.

## Scaling Databases
* Single Point of Failure: One failure could break the entire application.
* Database Partitioning
### Vertical Database Partitioning
* Decrease the number of columns.
ex: flights -> flights, locations (FK)
### Horizontal Database Partitioning
* Split up the rows of a table.
ex: flights -> flights_domestic, flights_international
Good for query speed
Bad for schema changes, query for all
### Database Sharding
ex) One database server for flights_domestic, another for flights_international
Good for query for all
Bad for JOIN
* Database Replication (Backup): Avoid single point of failure.
* Single-Primary Replication - Primary database(R/W), Secondary databases(R)
Whenever 'write' happens, you need to update secondary databases to stay in sync.
Good for Read
Bad for Write
* Multi-Primary Replication
Good for single point failure
Bad for update(sync), race condition

## Caching
* Take data and information and store it in some temporary place for usage later.
Good for persistent page
Bad for capricious page (Need hard refresh)
### Client-Side Caching
* In general, JavaScript files are stored in client side.
(HTTP response headers)
```
Cache-Control: max-age=86400
ETag: "7477656E74796569676874"
```
* Browser can check 'ETag'(a version of a resource) to decide whether or not to hard refresh the page.
* If 'ETag' matches up, respond with HTTP status code 304 Not Modified.
* Good for faster load (client side), less resource (server side)
* Bad for privacy.
### Server-Side Caching
* Cache is most likely faster than the database.
* Using Cache uses less resource than doing wth database.
ex) The 10 most popular books
* Cache Invalidation: Cache data does not match with database.
* Cache can be stored externally(an independent server) or internally(a physical file).

* ApacheBench: a software for benchmarking