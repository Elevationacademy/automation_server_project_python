from flask import request, Blueprint, Response
import json

api = Blueprint('api', __name__, template_folder='templates')

with open("pokemon.json", 'r') as j:
    pokemons = json.load(j)

pokemon_DB = []
for pokemon in pokemons:
    pokemon_DB.append(
        {"id": pokemon["id"], "name": pokemon["name"], "type": pokemon["type"], "height": pokemon["height"],
         "weight": pokemon["weight"]})


# GET
@api.route('/pokemon', methods=["GET"])
def get_pokemons():
    type = request.json['type']
    value = request.json['value']
    if type == "id" or type == "height" or type == "weight":
        value = int(value)
    results = list(filter(lambda x: x[type] == value, pokemon_DB))
    return Response(json.dumps(results))


# PUT
@api.route('/pokemon', methods=["PUT"])
def put_pokemon():
    type = request.json['type']
    value = request.json['value']
    type_to_change = request.json['type_to_change']
    value_to_change = request.json['value_to_change']
    entirety = not (type == None or value == None or type_to_change == None or value_to_change == None)
    if not entirety:
        return Response("Some details are missing")

    if type == "id" or type == "height" or type == "weight":
        value = int(value)
    if type_to_change == "id" or type_to_change == "height" or type_to_change == "weight":
        value_to_change = int(value_to_change)

    is_pokemon = False
    for pokemon in pokemon_DB:
        if pokemon[type] == value:
            pokemon[type_to_change] = value_to_change
            is_pokemon = True
    if is_pokemon:
        return Response(
            f"A pokemon with {type} of {value} was changed. His {type_to_change} was changed to {value_to_change}")
    else:
        return Response(f"A pokemon with {type} of {value} was not found")


# POST
@api.route('/pokemon', methods=["POST"])
def post_pokemon():
    id = request.json['id']
    name = request.json['name']
    type = request.json['type']
    height = request.json['height']
    weight = request.json['weight']
    is_id_exists = bool(len(list(filter(lambda x: x["id"] == id, pokemon_DB))))
    entirety = not (id == None or name == None or type == None or height == None or weight == None)
    if is_id_exists:
        return Response(f"A pokemon with id of {id} is already exist")
    elif entirety:
        pokemon_DB.append({"id": id, "name": name, "type": type, "height": height, "weight": weight})
        return Response(
            f"A new pokemon with id of {id} was added--->  Name: {name} ; Type: {type} ; Height: {height} ; Weight: {weight}")
    else:
        return Response("One or more of the details are missing or invalid")


# DELETE
@api.route('/pokemon', methods=["DELETE"])
def delete_pokemon():
    id = request.json['id']
    if id == None:
        return Response("The id is missing")
    for index in range(0, len(pokemon_DB)):
        if pokemon_DB[index]["id"] == id:
            pokemon_DB.pop(index)
            return Response(f"A pokemon with id of {id} was deleted")
    return Response(f"A pokemon with id of {id} was not found")
