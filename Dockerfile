FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /threadhub
WORKDIR /threadhub

ADD . /threadhub/

RUN pip install poetry

COPY poetry.lock pyproject.toml /threadhub/

RUN poetry config virtualenvs.create false
RUN poetry install


EXPOSE 8080

ENTRYPOINT ["python", "threadhub/manage.py"]
CMD ["runserver", "0.0.0.0:8080"]