# drf-demo
A simple example django application demonstrating Django Rest Framework exposed api with simple jwt authorization

## Application Summary
This application defines two models which are `Invoice` and `Product` and uses `User` from `django.contrib.auth.models`
for the purpose of users' authentication and authorization.

Django Rest Framework is used to expose models `Invoice` and `Product` through a REST API via `api/invoices/` and `api/products/` respectively
accepting GET POST PUT DELETE and other HTTP request methods, in which it can mainly view, update, insert or delete data from the database.

For the purpose of demostration `api/products/` can be accessed without authentication however model `api/invoices/` requires 
an authenticated user (a valid JWT Authorization Header with request).

## Fixture Data
Some fixture data are defined in _fixtures.py_ in order to be added to the database and experimented with.

Users to aquire `JWT token` with:

| username | password |
|----------|----------|
| rawad    | 1234     |
| admin    | 1234     |

## Run Application

After cloning this repository you can run the application using:

```bash
$ virtualenv -p python3.5 env
$ . ./env/bin/activate
$ cd demo/
$ python manage.py migrate
$ python fixtures.py
$ python manage.py runserver
```

## Curl Tests

### JWT Authorization

Following are some failing attempts to aquire a `JWT token`

```bash
$ curl -X POST  http://localhost:8000/auth-jwt/
{"password":["This field is required."],"username":["This field is required."]}

$ curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"8971234"}' http://localhost:8000/auth-jwt/
{"non_field_errors":["Unable to log in with provided credentials."]}

```

Following is a successful attempt to aquire a `JWT token`

```bash
# get jwt token for user rawad with password 1234
$ curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"1234"}' http://localhost:8000/auth-jwt/
```

### Django Rest Framework API

Following is are some failing attempts to get data from table products

```bash
# with no jwt token
$ curl -X GET http://localhost:8000/api/products/
{"detail":"Authentication credentials were not provided."}

# invalid jwt token
$ curl -X GET -H 'Authorization: Bearer some.invalid.token' http://localhost:8000/api/products/
{"detail":"Error decoding signature."}
```

Following is a successful attempt to get data from table products providing a valid `JWT token`

```bash
# get jwt token
$ curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"1234"}' http://localhost:8000/auth-jwt/

# export jwt token to environment
$ export rawad_jwt=$(curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"1234"}' http://localhost:8000/auth-jwt/ | awk -F'"' '{print $4}')

# use jwt token to get products
$ curl -X GET -H 'Authorization: Bearer '$rawad_jwt http://localhost:8000/api/products/
[{"product_pk":1,"name":"car","price":10200.0,"dummy":"","created_by":1,"created_at":"2017-08-11T10:53:35.380454Z"},{"product_pk":2,"name":"carpet","price":200.0,"dummy":"","created_by":1,"created_at":"2017-08-11T10:53:35.388016Z"},{"product_pk":3,"name":"cartridge","price":20.0,"dummy":"","created_by":1,"created_at":"2017-08-11T10:53:35.394368Z"}]
```

