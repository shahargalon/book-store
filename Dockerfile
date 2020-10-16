FROM python:3

WORKDIR /usr/src/app
COPY Pipfile.lock Pipfile src ./
RUN pip install pipenv && pipenv install --system --dev  --ignore-pipfile
EXPOSE 8000

CMD [ "python", "server.py" ]

