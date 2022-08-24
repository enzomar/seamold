FROM python:3.10

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD {{cookiecutter.project}} /app

CMD ["python", "{{cookiecutter.project}}.py"]