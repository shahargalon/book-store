# Book Store

The backend for an awesome book store app!

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/shahargalon/book-store/CI-workflow%20to%20run%20test%20on%20the%20code?label=CI-workflow&logo=GitHub)

## Pre Requirements

1. [Python](https://www.python.org).
2. [Pipenv](https://docs.pipenv.org/).

## Development

1. Create a virtual environment and activate it `pipenv shell`.
2. Install all dependencies `pipenv install`.
3. Run the server with `python src/server.py`.
4. Open an HTTP client at hit [http://localhost:8000](http://localhost:8000).

# Production

In production don't use the `sanic` server, use something like [gunicorn](https://docs.gunicorn.org) (read [this](https://vsupalov.com/what-is-gunicorn)). Use it like so:

```bash
$ gunicorn server:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker
```

## Tests

To run the linter

```bash
$ pycodestyle .
```

To run the tests

```bash
$ python -m unittest
```
