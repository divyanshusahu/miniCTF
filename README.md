# MINICTF

### A platform build in django for hosting CTF events. 

#### Test it [here](https://dashboard.heroku.com/apps)

#### FEATURES :

* Simple Interface
* Score Board
* Responsive Design
* and lots of other cool features.

#### SCREENSHOTS :

Challenge Page

<img src="readmeimg/challenges.png" width="100%">

Challenge View

<img src="readmeimg/onechallenge.png" width="100%">

#### Test it locally

###### Requirments

```
python 3.5.x
django 2.0
```

###### Install

```
git clone
django-admin startproject minictf
copy all folders inside git clone to django project folder
python manage.py makemigrations accounts challenges
python manage.py migrate
python manage.py runserver
```
