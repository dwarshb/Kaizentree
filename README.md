# Kaizentree

A Django application that includes Authentication and Dashboard to display a list of items and their stock status. It uses SQL database as it is setup by default when creating a Django project and it is easy to use. It also includes APIs which can be used to add the items and category.

# Prerequisites
- Install Python 3.11 on your System

# Installation 
- Step 1: Clone the library using 'git clone https://github.com/dwarshb/Kaizentree.git' in your terminal
- Step 2: Redirect to folder and use `python3 manage.py collectstatic`
- Step 3: `python3 manage.py makemigrations`
- Step 4: `python3 manage.py migrate`
- Step 5: `python3 manage.py runserver`

# Demo
[![Demo VIDEO](https://img.youtube.com/vi/_Au7RDCmKks/0.jpg)](https://www.youtube.com/watch?v=_Au7RDCmKks)

# APIs
Below are the list of APIs available which can used to perform certain operations.
 - To create a user
```
curl --location 'https://kaizentree.onrender.com/api/createuser/' \
--header 'Content-Type: application/json' \
--data-raw '{"username": "test2","email":"test2@gmail.com","password":"test123"}'
```

- To add new category
 ```
 curl --location 'https://kaizentree.onrender.com/api/category/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3ODAxODQyLCJpYXQiOjE3MDc4MDE1NDIsImp0aSI6IjhkNGNhMzIxM2ZlZjQyN2M4Nzg5N2ZhZmYzYzhkZDJmIiwidXNlcl9pZCI6Mn0.p9b69w9oVgvOmHFbC7kp4jiEnoIgLth11mrmjJCOmVE' \
--data '{"name": "Category 3"}'
```

- To add new item
```
curl --location 'https://kaizentree.onrender.com/api/item/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3ODAzNjAzLCJpYXQiOjE3MDc4MDMzMDMsImp0aSI6Ijg3NWM0NTc5M2I5MzQyOTliYjY5N2NmNThhYTczN2E2IiwidXNlcl9pZCI6Mn0.fY8NW8pAw0iDgvUvkX89jYxCIX_cfNrvG3R_DNBkqPw' \
--header 'Content-Type: application/json' \
--data '{
    "sku":"NY-STOCK",
    "name": "NY BEESWAX BUNDLE",
    "tags":[1],
    "category":[5],
    "in_stock":2000,
    "available_stock":2000
}'
```

# Testcase
To run testcase, you can use `python3 manage.py test`
