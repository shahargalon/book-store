FROM python:3

WORKDIR /usr/src/app
COPY ./. .
RUN pip install pipenv && pip install -U python-dotenv && pipenv install --system --ignore-pipfile
EXPOSE 8000
EXPOSE 5432

CMD [ "gunicorn", "src.server:app",  "--bind", "0.0.0.0:8000", "--worker-class", "sanic.worker.GunicornWorker" ] 
