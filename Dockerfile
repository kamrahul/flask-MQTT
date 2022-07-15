FROM python:3.9

COPY requirements.txt /src/requirements.txt
WORKDIR /src/

RUN pip install -r requirements.txt
COPY . /src
EXPOSE 5000

ENTRYPOINT [ "gunicorn","run:app","-w","1","--bind","0.0.0.0:5000" ]