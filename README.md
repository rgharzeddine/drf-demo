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
{
    "password": [
        "This field is required."
    ],
    "username": [
        "This field is required."
    ]
}

$ curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"8971234"}' http://localhost:8000/auth-jwt/
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

Following is a successful attempt to aquire a `JWT token`

```bash
# get jwt token for user rawad with password 1234
$ curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"1234"}' http://localhost:8000/auth-jwt/
```

### Django Rest Framework API

Following is are some failing attempts to get data from table invoices

```bash
# with no jwt token
$ curl -X GET http://localhost:8000/api/invoices/
{
    "detail": "Authentication credentials were not provided."
}

# invalid jwt token
$ curl -X GET -H 'Authorization: Bearer some.invalid.token' http://localhost:8000/api/invoices/
{
    "detail": "Error decoding signature."
}
```

Following is a successful attempt to get data from table invoices providing a valid `JWT token`

```bash
# get jwt token
$ curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"1234"}' http://localhost:8000/auth-jwt/
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InJhd2FkIiwiZW1haWwiOiIiLCJleHAiOjE1MDI3MTI0MjN9.jvYKSbTphhsgTwl_GABA8-wGbCYO6rosB2dduqokYQ8"
}

# export jwt token to environment
$ export rawad_jwt=$(curl -X POST -H "Content-Type: application/json" -d '{"username":"rawad","password":"1234"}' http://localhost:8000/auth-jwt/ | awk -F'"' '{print $4}')

# use jwt token to get invoices
$ curl -X GET -H 'Authorization: Bearer '$rawad_jwt http://localhost:8000/api/invoices/
[
    {
        "invoice_pk": 1,
        "name": "",
        "type": "In",
        "amount": 50000.0,
        "dummy": "",
        "salesman": 3,
        "created_by": 2,
        "created_at": "2017-08-11T12:11:57.020803Z"
    },
    {
        "invoice_pk": 2,
        "name": "",
        "type": "Out",
        "amount": 60000.0,
        "dummy": "",
        "salesman": 4,
        "created_by": 2,
        "created_at": "2017-08-11T12:11:57.026795Z"
    },
    {
        "invoice_pk": 3,
        "name": "",
        "type": "In",
        "amount": 20500.0,
        "dummy": "",
        "salesman": 4,
        "created_by": 1,
        "created_at": "2017-08-11T12:11:57.032723Z"
    }
]
```