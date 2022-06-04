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
### نتیجه نمایش داده شده تمامی کتابهای موجود در سیستم است(رزرو و غیر رزرو)

- result : 

``` json
[
    {
        "id": 1,
        "title": "پیرمرد و دریا",
        "slug": "The-Old-Man-and-the-Sea",
        "description": "کتاب پیرمرد و دریا با عنوان اصلی The Old Man and the Sea اثری شگفت‌انگیز، هنرمندانه و زیبا از نویسنده بزرگ آمریکایی، ارنست همینگ‌وی است. این «رمان کوتاه» که نویسنده‌اش آن را عصاره همه زندگی و هنرش می‌داند، مفهوم تازه‌ای از شکست و موفقیت پیش چشمان شما باز می‌کند و ما خواندن آن را با ترجمه ناب نجف دریابندری به همه پیشنهاد می‌کنیم. همینگ‌وی در سال ۱۹۵۴ جایزه نوبل ادبیات را نیز از آن خود کرد. موسسه نوبل در وصف کارهای او و علت اهدا این جایزه می‌نویسد: «به خاطر استادی در روایت هنرمندانه، که اخیراً در پیرمرد و دریا نشان داد و اعمال نفوذ او در سبک معاصر.»",
        "photo": "/media/images/book/2022/06/02/Oldmansea.jpg",
        "release_date": 1951,
        "reserve": false,
        "athore": 1,
        "genre": [
            2
        ]
    },
    {
        "id": 2,
        "title": "آنا کارنینا",
        "slug": "ana-karenia",
        "description": "نا کارنینا نوشته نویسنده مشهور قرن نوزدهم لئون تالستوی است. کتابی که برخی منتقدان آن را بهترین رمان تاریخ دانسته‌اند و یا همواره آن را در لیست ده کتاب برتر تاریخ قرار می‌دهند. تولستوی در رمان آنا کارنینا شرح حال روابط میان خانواده‌های روسی در قرن نوزدهم را روایت می‌کند. کتابی که هرکسی در طول زندگی‌اش حتما باید آن را بخواند. ما نیز در کافه‌بوک این رمان برجسته را در لیست کتاب‌های پیشنهادی کافه‌بوک قرار داده‌ایم.",
        "photo": "/media/images/book/2022/06/02/ana-carani.png",
        "release_date": 1875,
        "reserve": true,
        "athore": 2,
        "genre": [
            5
        ]
    },
    {
        "id": 3,
        "title": "رمان طاعون",
        "slug": "rmn-taaon",
        "description": "کتاب طاعون اثر برجسته نویسنده برنده جایزه نوبل، آلبر کامو است که در سال ۱۹۴۷ به چاپ رسید. در این رمان، شخصیت‌های داستان علیه بی‌عدالتی جهان دست به عصیان می‌زند. کامو درباره این کتاب در نامه‌ای به رولان بارت می‌نویسد: «در مقایسه با رمان بیگانه، طاعون بی گفتگو گذاری است از سرکشی انفرادی به جهان اجتماعی، اجتماعی که باید در مبارزه‌هایش شرکت کرد. اگر از بیگانه تا طاعون راهی در راستای تحول باشد، این تحول در جهان همبستگی و مشارکت است.»",
        "photo": "/media/images/book/2022/06/02/tauon.png",
        "release_date": 1947,
        "reserve": true,
        "athore": 3,
        "genre": [
            2,
            4
        ]
    },
    {
        "id": 4,
        "title": "رمان سفرهای گالیور",
        "slug": "rmn-sfrh-lor",
        "description": "کتاب سفرهای گالیور از جمله مشهورترین رمان‌های کلاسیک است که در آن، نویسنده ما را به سفرهایی شگفت‌انگیز می‌برد. سفر به مکان‌هایی که باعث می‌شود کتاب به اولین رمان پادآرمان‌شهر در دنیای ادبیات کلاسیک بدل شود. راز ماندگاری مشهورترین اثر جاناتان سوییفت در این است که قهرمان خارق‌العاده‌اش در دنیای تمثیل‌ها حبس نمی‌شود، چرا که نویسنده میراثی چند وجهی در تاریخ ادبیات خلق کرده است. در این کتاب، سوییفت با استفاده از تمثیل نقدهای زیادی به حاکمیت، مذهب و جامعه انسانی وارد می‌کند.",
        "photo": "/media/images/book/2022/06/02/galiver.png",
        "release_date": 1670,
        "reserve": false,
        "athore": 4,
        "genre": [
            2
        ]
    },
    {
        "id": 5,
        "title": "رمان سفرهای گالیور",
        "slug": "ronan-safar-galiver",
        "description": "کتاب سفرهای گالیور از جمله مشهورترین رمان‌های کلاسیک است که در آن، نویسنده ما را به سفرهایی شگفت‌انگیز می‌برد. سفر به مکان‌هایی که باعث می‌شود کتاب به اولین رمان پادآرمان‌شهر در دنیای ادبیات کلاسیک بدل شود. راز ماندگاری مشهورترین اثر جاناتان سوییفت در این است که قهرمان خارق‌العاده‌اش در دنیای تمثیل‌ها حبس نمی‌شود، چرا که نویسنده میراثی چند وجهی در تاریخ ادبیات خلق کرده است. در این کتاب، سوییفت با استفاده از تمثیل نقدهای زیادی به حاکمیت، مذهب و جامعه انسانی وارد می‌کند.",
        "photo": "/media/images/book/2022/06/02/galiver_MlY0q1Z.png",
        "release_date": 1670,
        "reserve": false,
        "athore": 4,
        "genre": [
            2
        ]
    }    
]
  ```
  
  
  ## گرفتن اطلاعات یک کتاب : 
   - GET
- لینک درخواست :
-   ```http://127.0.0.1:8000/api/1```

درخواست با پایتون : 
```
response = requests.get('http://127.0.0.1:8000/api/1')
print(response.json())
```
### نتیجه نمایش یک کتاب 

- result : 
  
 ``` json
{
    "id": 1,
    "title": "پیرمرد و دریا",
    "slug": "The-Old-Man-and-the-Sea",
    "description": "کتاب پیرمرد و دریا با عنوان اصلی The Old Man and the Sea اثری شگفت‌انگیز، هنرمندانه و زیبا از نویسنده بزرگ آمریکایی، ارنست همینگ‌وی است. این «رمان کوتاه» که نویسنده‌اش آن را عصاره همه زندگی و هنرش می‌داند، مفهوم تازه‌ای از شکست و موفقیت پیش چشمان شما باز می‌کند و ما خواندن آن را با ترجمه ناب نجف دریابندری به همه پیشنهاد می‌کنیم. همینگ‌وی در سال ۱۹۵۴ جایزه نوبل ادبیات را نیز از آن خود کرد. موسسه نوبل در وصف کارهای او و علت اهدا این جایزه می‌نویسد: «به خاطر استادی در روایت هنرمندانه، که اخیراً در پیرمرد و دریا نشان داد و اعمال نفوذ او در سبک معاصر.»",
    "photo": "http://127.0.0.1:8000/media/images/book/2022/06/02/Oldmansea.jpg",
    "release_date": 1951,
    "reserve": false,
    "athore": 1,
    "genre": [
        2
    ]
}
 ```
  
 
 
  

##  متد های بعدی نیازمند لاگین و یا داشتن توکن هستن . 

### رجیستر کردن با api و دریافت توکن برای درخواست های بعد :


   - POST
- لینک درخواست :
-   ```http://127.0.0.1:8000/api/register/```

درخواست با پایتون : 
```

  HEADER = {
      "Content-Type": "application/json",
  }
  DATA = {
          "username": "user1",
          "email": "user1@gmail.com",
          "password": "pa55word"
      }
  response = requests.post('http://127.0.0.1:8000/api/register/', headers=HEADER, data=json.dumps(DATA))
  print(response.json())
```
### نتیجه ریجستر موفق کاربر 

- result : 
  
 ``` json
{"Token": "b65a24acc9eee40b5ddf9952bfb4bfe13eb86866", "Message": "Register Success"}

 ```



### گرفتن لیست کتابهای رزرو شده توسط کاربر  :


   - GET
- لینک درخواست :
-   ```http://127.0.0.1:8000/api/orders/```

درخواست با پایتون : 
```

  HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token b65a24acc9eee40b5ddf9952bfb4bfe13eb86866",
  }
  response = requests.get('http://127.0.0.1:8000/api/orders/', headers=HEADER)
  print(response.json())
```
### نتیجه : ما دو کتاب رزرو کرده ایم.    

- result : 
  
 ``` json
[
    {
        "id": 68,
        "reserv_date": "2022-06-04T15:59:58.411501Z",
        "is_reserve": true,
        "user": 1,
        "book": 1
    },
    {
        "id": 69,
        "reserv_date": "2022-06-04T16:00:16.432125Z",
        "is_reserve": true,
        "user": 1,
        "book": 5
    }
]
 ```





### رزرو کتاب توسط کاربر  :


   - POST
- لینک درخواست :
-   ```http://127.0.0.1:8000/api/order/add/```

درخواست با پایتون : 
```

  HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token b65a24acc9eee40b5ddf9952bfb4bfe13eb86866",
  }
  DATA = {
        "is_reserve": True,
        "user": "1",
        "book": "5"
    }
  response = requests.get('http://127.0.0.1:8000/api/order/add/', headers=HEADER, data=json.dumps(DATA))
  print(response.json())
```
### نتیجه : اگر کتاب از قبل رزرو نشده باشد به صورت زیر است.    

- result : 
  
 ``` json
 {
    "id": 70,
    "reserv_date": "2022-06-04T16:05:34.550885Z",
    "is_reserve": true,
    "user": 1,
    "book": 6
}

 ```
 









    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 7062a10bde0cfba6b3692f8451b5f7c730a55a4e",
    }
    DATA = {
            "is_reserve": True,
            "user": "1",
            "book": "5"
        }
    # response = requests.post('http://127.0.0.1:8000/api/order/add/', headers=HEADER, data=json.dumps(DATA))
    # print(response.json())




![api_all_book](http://i.imgur.com/WqnREXr.png "api_all_book")







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
  
  





