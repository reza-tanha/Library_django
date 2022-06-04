# Library_django

### راهنمای استفاده از api:‌



## دیدن لیست کل کتاب ها

متد مجاز: 
  - GET
- لینک درخواست :
-   ```http://127.0.0.1:8000/api/```

http://127.0.0.1:8000/api/
## api usage guide

### books list api

- All books available on the site
- method 
  - GET
- login required
- path : 
-  ```127.0.0.1:8000/api/```


### book detail api

- Information of a book
- method
  -  GET
- login required
- path : 
- ```127.0.0.1:8000/api/1```



### user books reserve

- method
  -  GET
- login required
- path : 
- ```127.0.0.1:8000/api/orders/```


### Order a book

- method
  -  POST
- login required
- path : 
-  ```127.0.0.1:8000/api/orders/add/```
  
  ```
  data = {
    'user': <user id>, 
    'book': <book id>, 
    'is_reserve': true
  }
  ```
  

### delete Order from user orders 

- method
  -  DELETE
- login required
- path : 
-  ```127.0.0.1:8000/api/orders/delete/<order id>```
  
  





