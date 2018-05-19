# ABME


### 1. Usage
#### &nbsp;&nbsp;&nbsp;&nbsp;1.1. Live Version
&nbsp;&nbsp;&nbsp;&nbsp;Hosted in cloud server http://abme.herokuapp.com/
#### &nbsp;&nbsp;&nbsp;&nbsp;1.2. Get it local!
###### &nbsp;&nbsp;&nbsp;&nbsp;Clone it
&nbsp;&nbsp;&nbsp;&nbsp;`$ mkdir abme_folder & cd abme_folder`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`$ git clone https://github.com/b1oader/abme.git`
###### &nbsp;&nbsp;&nbsp;&nbsp;Virtual Environment
&nbsp;&nbsp;&nbsp;&nbsp;install<br>
&nbsp;&nbsp;&nbsp;&nbsp;`$ pip install virtualenv`<br>
&nbsp;&nbsp;&nbsp;&nbsp;create<br>
&nbsp;&nbsp;&nbsp;&nbsp;`$ virtualenv abme`<br>
&nbsp;&nbsp;&nbsp;&nbsp;run<br>
&nbsp;&nbsp;&nbsp;&nbsp;`$ abme\scripts\activate`<br>
###### &nbsp;&nbsp;&nbsp;&nbsp;Requirements
&nbsp;&nbsp;&nbsp;&nbsp;`$ pip install -r requirements.txt`<br>
###### &nbsp;&nbsp;&nbsp;&nbsp;Migrations & runserver
&nbsp;&nbsp;&nbsp;&nbsp;`$ python manage.py makemigrations`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`$ python manage.py migrate`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`$ python manage.py runserver`<br>
### 2. Used technologies
* Python 3.6
  * Django 1.11
  * Django REST framework
* HTML5
* CSS
  * Bootstrap 4
* Javascript
  * Jquery
  * Ajax
* Database
  * SQLite (local)
  * PostgreSQL (heroku)
### 3. Database visualization
![alt text](https://i.imgur.com/I8oT51U.png)
