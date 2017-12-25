# MINICTF

### A platform build in django for hosting CTF events. 

#### Live demo 

###### Available Soon

#### Test it locally

Here in this branch I added my own database which I used in the development process. Therefore admin and other users are already there with some challenges to test. Below are the few credentials to use. 

```
thrones:12345678
testing:12345678
```

###### Install miniCTF

```sh
$ git clone https://github.com/DivyanshuSahu/miniCTF.git
$ git checkout local # switch to local branch
$ django-admin startproject minictf
copy all files and folders from git clone folder(miniCTF) to django project folder(minictf)
$ python manage.py runserver
```

Then use above credentials to log in.
