FROM python:3

RUN pip install pipenv
WORKDIR /usr/src/app
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 8000
COPY server.py .
CMD [ "python", "server.py" ]

