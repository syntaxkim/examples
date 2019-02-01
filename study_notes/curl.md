# cURL
2018-11-09

**cURL provides a library and command-line tool for transferring data using various protocols.**

### User-related routes
1. create_user
curl -H 'Content-Type: application/json' -d '{"name": "admin", "password": "password"}' 127.0.0.1:5000/users
curl -H 'Content-Type: application/json' -d '{"name": "user0", "password": "password"}' 127.0.0.1:5000/users
curl -H 'Content-Type: application/json' -d '{"name": "user1", "password": "password"}' 127.0.0.1:5000/users
curl -H 'Content-Type: application/json' -d '{"name": "user2", "password": "password"}' 127.0.0.1:5000/users

* Update admin user in psql
UPDATE users SET admin=true WHERE name='admin';

3. login
curl -u admin:password 127.0.0.1:5000/login
curl -u user0:password 127.0.0.1:5000/login
curl -u user1:password 127.0.0.1:5000/login
curl -u user2:password 127.0.0.1:5000/login
curl -v -u user3:password 127.0.0.1:5000/login (Could not verify)

4. get_users
curl 127.0.0.1:5000/users ((Token is missing)
curl -H x-access-token:admin_t0ken 127.0.0.1:5000/users (200)
curl -H x-access-token:user0_t0ken 127.0.0.1:5000/users ("Not authorized")
curl -H x-access-token:random_t0ken 127.0.0.1:5000/users ("Token is invalid")

5. get_user
curl -H x-access-token:admin_t0ken 127.0.0.1:5000/users/user0_public_id (200)
curl -H x-access-token:admin_t0ken 127.0.0.1:5000/users/random_id ("No user found")
curl -H x-access-token:user0_t0ken 127.0.0.1:5000/users/any_id ("Not authorized")

5. update_user
curl -X PUT -H x-access-token:admin_t0ken 127.0.0.1:5000/users/user0_public_id ("User updated") -> ("Already updated")
curl -X PUT -H x-access-token:admin_t0ken 127.0.0.1:5000/users/random_id ("No user found")
curl -X PUT -H x-access-token:user1_t0ken 127.0.0.1:5000/users/any_id ("Not authorized")

6. delete_user
curl -X DELETE -H x-access-token:admin_t0ken 127.0.0.1:5000/users/user0_public_id ("User deleted") -> ("No user found")
curl -X DELETE -H x-access-token:admin_t0ken 127.0.0.1:5000/users/random_id ("No user found")
curl -X DELETE -H x-access-token:user1_t0ken 127.0.0.1:5000/users/any_id ("Not authorized")

### Task-related routes
1. create_task
curl -H Content-Type:application/json -H x-access-token:user1_token -d '{"task": "Study!"}' 127.0.0.1:5000/tasks
curl -H Content-Type:application/json -H x-access-token:user1_token -d '{"task": "Study more!"}' 127.0.0.1:5000/tasks
curl -H Content-Type:application/json -H x-access-token:user1_token -d '{"task": "Rest!"}' 127.0.0.1:5000/tasks

2. get_tasks
curl -H x-access-token:user1_token 127.0.0.1:5000/tasks
curl -H x-access-token:user2_token 127.0.0.1:5000/tasks ("No task to do")

3. get_task
curl -H x-access-token:user1_token 127.0.0.1:5000/tasks/1
curl -H x-access-token:user1_token 127.0.0.1:5000/tasks/2
curl -H x-access-token:user1_token 127.0.0.1:5000/tasks/3
curl -H x-access-token:user1_token 127.0.0.1:5000/tasks/4 ("No task found")
curl -H x-access-token:user2_token 127.0.0.1:5000/tasks/4 ("No task found")

4. complete_task
curl -X PUT -H x-access-token:user1_token 127.0.0.1:5000/tasks/1 ("Task completed")
curl -X PUT -H x-access-token:user1_token 127.0.0.1:5000/tasks/1 ("Already completed")
curl -X PUT -H x-access-token:user1_token 127.0.0.1:5000/tasks/4 ("No task found")

5. delete_task
curl -X DELETE -H x-access-token:user1_token 127.0.0.1:5000/tasks/3 ("Task deleted")
curl -X DELETE -H x-access-token:user1_token 127.0.0.1:5000/tasks/3 ("No task found")
curl -X DELETE -H x-access-token:user1_token 127.0.0.1:5000/tasks/4 ("No task found")


### Notes
You muste include the admin's token into the header in order to use admin functions
'-H x-access-token:admin_t0ken'

### Basic commands
* Send GET request and show body
curl <url>

* Send GET request and show response header only
curl -I <url>

* Send GET request and show headers and contents
curl -v <url>

* Send custom header data
curl -H <custom_header> <url>

* Send custom request (default: GET, hidden, no need to use when using -d to POST)
curl -X <request_method> <url>

* Send JSON data using POST
curl -H 'Content-Type: application/json' -d '{"name": "admin", "password": "password"}' <url>

* Send data with 'Content-Type: multipart/form-data' (filled-in form in web browser)
curl -F name=admin -F password=password <url>

* Server authentication
curl -u <user:password> <url>