FROM python:3.8

WORKDIR /usr/local/django

COPY requirements.txt . 
# install our two dependencies
RUN pip install -r requirements.txt

# copy our project code
COPY ./django_app  .

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "django_app", "--workers", "5","--bind", ":8000", "django_app.wsgi:application"]
