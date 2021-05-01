FROM python:3.7

COPY ./requirements.txt /sys-employees/requirements.txt

WORKDIR /sys-employees

RUN pip install -r requirements.txt

COPY . /sys-employees

EXPOSE 9000

CMD [ "sh", "-c", "gunicorn api.app:app --bind 0.0.0.0:9000" ]
