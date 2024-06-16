FROM ubuntu:latest

RUN apt update -y && \
    apt install -y python3 python3-pip

RUN pip install poetry==1.4.2
RUN poetry config installer.max-workers 10

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /usr/iot/

COPY pyproject.toml poetry.lock ./

RUN poetry install  --without dev --no-root --no-interaction --no-ansi -vvv && rm -rf $POETRY_CACHE_DIR

COPY ./app/ ./app/

EXPOSE 5000

CMD ["poetry", "run", "run-engine"]