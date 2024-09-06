# pull official base image
FROM python:3.10-bullseye

# set work directory
WORKDIR /srv/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

# install system dependencies
RUN apt-get update && apt-get install -y \
  gcc \
  netcat \
  libpq-dev \
  postgresql-client \
  curl \
  && apt-get clean

# install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# copy pyproject.toml and poetry.lock
COPY ./pyproject.toml ./poetry.lock ./

# install dependencies
RUN poetry install --no-root

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# make entrypoint.sh executable
RUN chmod +x /srv/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/srv/app/entrypoint.sh"]