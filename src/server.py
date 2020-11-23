from peewee import *
from sanic import Sanic
from sanic.response import json

app = Sanic(name="awesome_book_store")
psql_db = PostgresqlDatabase('book_store', user='nirgalon')


class Person(Model):
    first_name = CharField()
    last_name = CharField()
    age = IntegerField()

    class Meta:
        database = psql_db


@app.route('/person', methods=["POST"])
async def create_person(request):
    new_person = Person(
        first_name=request.json["first_name"],
        last_name=request.json["last_name"],
        age=int(request.json["age"]),
    )
    new_person.save()
    return json(new_person)


@app.route('/person',)
async def create_person(request):
    persons = Person.select()
    return json(persons)


@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
