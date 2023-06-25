## Flask with MySql
### You can find the ERD.png which shows the database schema design in the root directory.
### You can find the table creation commands at create_tables.sql file in the root directory.
#### Prerequisite
##### 1. Docker: https://www.docker.com/products/docker-desktop/

#### Running steps:
1. In the root directory write in the terminal
```
docker compose up
```

Which will launch MySql container and the app container.

The app container has 4 APIs.
### List customer API:
#### Path: /<int:id>
#### Method: GET

### Create customer:
#### Path: /create_customer
#### Method: POST
#### Body: customer data

### Update customer:
#### Path: /update_customer/<int:id>
#### Method: PUT
#### Body: customer data

### Delete customer:
#### Path: /delete_customer/<int:id>
#### Method: DELETE
