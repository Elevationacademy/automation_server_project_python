import requests


class ApiManager:
    # Recieve type ("id" / "name" / "type" / "height" / "weight") and value (number or string)
    # Return an dict with a key of "status" (status code) and a key of "body" (array of dicts with the filtered pokemons)
    def get_pokemons(self, type, value):
        response = requests.get(
            'http://localhost:5000/pokemon',
            json={'type': type, 'value': value},
        )
        return ({
            "status": response.status_code,
            "body": response.json() or response.text
        })

    # Recieve type ("id" / "name" / "type" / "height" / "weight"), value (number or string) - and find ONE pokemon that has those attributes
    # Recieve type_to_change ("id" / "name" / "type" / "height" / "weight"), value_to_change (number or string) - and change that attribute for the poken that was found
    # Return an dict with a key of "status" (status code) and a key of "body" (a message)
    def put_pokemon(self, type=None, value=None, type_to_change=None, value_to_change=None):
        response = requests.put(
            'http://localhost:5000/pokemon',
            json={'type': type, 'value': value, 'type_to_change': type_to_change, 'value_to_change': value_to_change},
        )
        return ({
            "status": response.status_code,
            "body": response.text
        })

    # Recieve id(number), name(string), type(string), height(number), weight(number)
    # Return an dict with a key of "status" (status code) and a key of "body" (a message)
    def post_pokemon(self, id=None, name=None, type=None, height=None, weight=None):
        response = requests.post(
            'http://localhost:5000/pokemon',
            json={'id': id, 'name': name, 'type': type, 'height': height, 'weight': weight},
        )
        return ({
            "status": response.status_code,
            "body": response.text
        })

    # Recieve an id (number) and delete the pokemon with that id
    # Return an dict with a key of "status" (status code) and a key of "body" (a message)
    def delete_pokemon(self, id=None):
        response = requests.delete(
            'http://localhost:5000/pokemon',
            json={'id': id},
        )
        return ({
            "status": response.status_code,
            "body": response.text
        })
