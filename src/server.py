from peewee import *
from sanic import Sanic
from sanic.response import json
from playhouse.shortcuts import model_to_dict

app = Sanic(name="awesome_book_store")
psql_db = PostgresqlDatabase('book_store', user="asdasdasdasdasdasdasd", password, host, port)


class Person(Model):
    first_name = CharField()
    last_name = CharField()
    age = IntegerField()

    class Meta:
        database = psql_db


with psql_db:
    psql_db.create_tables([Person])


@app.route('/person', methods=["POST"])
async def create_person(request):
    new_person = Person(
        first_name=request.json["first_name"],
        last_name=request.json["last_name"],
        age=int(request.json["age"]),
    )
    new_person.save()
    return json(model_to_dict(new_person))


@app.route('/person',)
async def create_person(request):
    persons = Person.select().dicts()
    results = [person for person in persons]
    return json(results)


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
