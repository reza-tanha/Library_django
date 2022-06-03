# Library_django

## api usage guide

### books list api

- All books available on the site
- method 
  - GET
- login required
- path : 
-   ```127.0.0.1:8000/api/```


### book detail api

Information of a book
method GET
login required
path : 
  ```127.0.0.1:8000/api/1```



### user orders reserve

method GET
login required
path : 
  ```127.0.0.1:8000/api/orders/```


### book order reserve

method GET
login required
path : 
  ```127.0.0.1:8000/api/orders/```


### Order a book

method POST
login required
path : 
  ```127.0.0.1:8000/api/orders/add/```
  
  ```
  data = {
    'user': <user id>, 
    'book': <book id>, 
    'is_reserve': true
  }
  ```
  

### delete Order from user orders 

method DELETE
login required
path : 
  ```127.0.0.1:8000/api/orders/delete/<order id>```
  
  





