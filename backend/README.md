# Backend

## Installation

```bash
pip intall poetry
poetry install
```


## Run

```zsh
poetry run uvicorn app.main:app --host=0.0.0.0 --port=8000 
```

---

## Test

```zsh
poetry run pytest
```

---

## Docker

```bash
docker build . --no-cache --tag backend
docker run -p 8000:8000 --name backend backend 
```

---

## Links

[http://localhost:8000](http://localhost:8000/)
[http://localhost:8000/docs#/](http://localhost:8000/docs#/)

