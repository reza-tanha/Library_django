# Library_django


#### Table of Contents
- **[Introduction](#introduction)**<br>
- **[Features](#features)**<br>
- **[Setup](#setup)**<br>
- **[Docker Setup](#docker-setup)**<br>
- **[Tests](#tests)**<br>
- **[TODO List](#todo)**<br>

<br>


## Introduction:
Library Django is a straightforward project that shows available books and lets you reserve books.<br>
If you have the required permissions you can add, delete the books in the Django admin or by the API.


## Features
- Drf RestApi: authenticate users and show, create, edit, and delete the books.
- Cloud: Optimized for deployments using Docker.
- WebServer: Configure Nginx caching, security, and compression.
- Swager: generate documentation for API.

<br>

## Setup
The first thing to do is to clone the repository:
```
- $ git clone https://github.com/reza-tanha/Library_django
- $ cd Library_django
````

Create a virtual environment to install dependencies in and activate it:
```
- $ virtualenv --no-site-packages env
- $ source env/bin/activate
```

Then install the dependencies:
```
- $ pip install requirments.txt
- $ cd config/
- $ python manage.py runserver
```
And navigate to http://127.0.0.1:8000/

<br>

## Docker Setup
First clone the repository:
```
- $ git clone https://github.com/reza-tanha/Library_django
- $ cd Library_django
```

Then user docker-compose tools to build and SetUp the containers.
```
- $ docker compose up
OR
- $ docker compose up -d 
To run containers in background
```
And navigate to http://127.0.0.1/

<br>

## Tests
To run the tests, cd into the directory where manage.py is:
```
- $ cd Library_django
- $ cd config/
- $ python manage.py test 
```


## TODO
- Add some fields to the book model like pages-number, rating, etc.
- Add a section to register and log in new users.
- Update templates
- ....


## guide use api
- **[show all books](#show-all-books)**<br>
- **[show one book](#show-one-book-)**<br>
- **[register and get token](#register-and-get-token-)**<br>
- **[show books reserve list](#show-books-reserve-list-)**<br>
- **[book reserve](#book-reserve-)**<br>
- **[book revoke](#book-revoke--)**<br>



## Show all books:

- GET
- Request Link :
-   ```http://127.0.0.1:8000/api/```


Request in pythn requests : 
```
response = requests.get('http://127.0.0.1:8000/api/')
print(response.json())
```

#### Result : 

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
  
  
## Show one book : 
- GET
- parameter [order id]
- Request Link :
```http://127.0.0.1:8000/api/<order id>```

Request in pythn requests : 
```
response = requests.get('http://127.0.0.1:8000/api/1')
print(response.json())
```
#### Result : 

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
  
 
 
  

#### in other Method  needed login or get token. 

## Register and get token :


- POST
- Request Link :
```http://127.0.0.1:8000/api/register/```

Request in pythn requests :  
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

#### Result : 
- result : 
  
 ``` json
{"Token": "b65a24acc9eee40b5ddf9952bfb4bfe13eb86866", "Message": "Register Success"}

 ```



## Show books reserve list :
- GET
- Request Link :  
```http://127.0.0.1:8000/api/orders/```

Request in pythn requests :  
```
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Token b65a24acc9eee40b5ddf9952bfb4bfe13eb86866",
}
response = requests.get('http://127.0.0.1:8000/api/orders/', headers=HEADER)
print(response.json())
```

#### Result : 
  
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


## Book reserve :

- POST
- data : <book , book-id>
- Request Link :  
```http://127.0.0.1:8000/api/order/add/```

Request in pythn requests :
```
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Token b65a24acc9eee40b5ddf9952bfb4bfe13eb86866",
}
DATA = {
    "book": "5"
}
response = requests.get('http://127.0.0.1:8000/api/order/add/', headers=HEADER, data=json.dumps(DATA))
print(response.json())
```

#### Result : 
  
 ``` json
 {
    "id": 70,
    "reserv_date": "2022-06-04T16:05:34.550885Z",
    "is_reserve": true,
    "user": 1,
    "book": 6
}

 ```
 

## Book revoke  :

- DELETE
- parameter [order id]
- Request Link :  
```http://127.0.0.1:8000/api/order/delete/<order id>```

Request in pythn requests :
```
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Token b65a24acc9eee40b5ddf9952bfb4bfe13eb86866",
}

response = requests.get('http://127.0.0.1:8000/api/order/delete/70', headers=HEADER)
print(response.json())
```
## Result :       
 ```
 "order Deleted"
 ```
 





