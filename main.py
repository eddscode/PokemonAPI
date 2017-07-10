from flask_api import FlaskAPI, exceptions
from pokemon import Pokemon

api = FlaskAPI(__name__)


@api.route("/<int:key>", endpoint='get_pokemon_name', methods=['GET'])
def get_pokemon_name(key):
    try:
        new_pokemon = Pokemon(key)
        return new_pokemon.get_name()
    except:
        raise exceptions.NotFound()


@api.route("/height/<int:key>", endpoint='get_pokemon_weight', methods=['GET'])
def get_pokemon_weight(key):
    try:
        new_pokemon = Pokemon(key)
        return new_pokemon.get_height()
    except:
        raise exceptions.NotFound()


@api.route("/weight/<int:key>", endpoint='get_pokemon_height', methods=['GET'])
def get_pokemon_weight(key):
    try:
        new_pokemon = Pokemon(key)
        return new_pokemon.get_weight()
    except:
        raise exceptions.NotFound()


@api.route("/base_experience/<int:key>", endpoint='get_base_experience', methods=['GET'])
def get_base_experience(key):
    try:
        new_pokemon = Pokemon(key)
        return new_pokemon.get_base_experience()
    except:
        raise exceptions.NotFound()

if __name__ == '__main__':
    api.run()
