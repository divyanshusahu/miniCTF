FROM python:3.8.13-slim-bullseye

RUN mkdir /code
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations accounts challenges forums
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
