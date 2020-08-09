FROM python:3.8.2
COPY /iStore /iStore
#COPY /requirements.txt /requirements.txt
WORKDIR iStore
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]