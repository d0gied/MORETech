FROM python:3.11.2-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

EXPOSE 8000
WORKDIR /code/

# install packages
RUN pip install poetry
COPY pyproject.toml /code/pyproject.toml
COPY poetry.lock /code/poetry.lock
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# copy source code
COPY app /code/app


CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
