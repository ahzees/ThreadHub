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


CMD ["ls" ,"threadhub",]