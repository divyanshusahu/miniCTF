# MINICTF

### A platform build in django for hosting CTF events. 

#### Live demo 

[website](https://dashboard.heroku.com/apps)

#### FEATURES :

* Cool Interface
* Score Board
* Responsive Design
* Email Conformation support
* Forgot password support
* and a lot more.

#### SCREENSHOTS :

Challenge Page

<img src="readmeimg/challenges.png" width="100%">

Challenge View

<img src="readmeimg/onechallenge.png" width="100%">

Score Board

<img src="readmeimg/scoreboard.png" width="100%">

Team Details

<img src="readmeimg/details.png" width="100%">

All Teams list

<img src="readmeimg/teams.png" width="100%">

#### Test it locally

###### Requirments

```
python 3.5.x
django 2.0
```

###### Install

```
git clone https://github.com/DivyanshuSahu/minictf.git
django-admin startproject minictf
copy all folders inside git clone to django project folder
python manage.py makemigrations accounts challenges
python manage.py migrate
python manage.py runserver
```
