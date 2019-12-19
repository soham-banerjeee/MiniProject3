import json

from flask import request

from database import *
from init import create_app
from models import Cats

app = create_app()


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 200


@app.route('/', methods=['GET'])
def fetch():
    cats = get_all(Cats)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200


@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200