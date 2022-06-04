# Library_django

### راهنمای استفاده از api:‌



## دیدن لیست کل کتاب ها

  - GET
- لینک درخواست :
-   ```http://127.0.0.1:8000/api/```

درخواست با پایتون : 
```
response = requests.get('http://127.0.0.1:8000/api/')
print(response.json())
```
# نتیجه نمایش داده شده تمامی کتابهای موجود در سیستم است(رزرو و غیر رزرو)

- result : 

! [api_all_book](http://i.imgur.com/WqnREXr.png, "api_all_book")







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
  
  





