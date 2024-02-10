#!/usr/bin/python3
"""nueva vista para cities"""

from flask import Flask, jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views

app = Flask(__name__)


@app.route('/api/v1/states//<state_id>/cities', methods=['GET'],
           strict_slashes=False)
def get_cities_by_states(state_id):
    # Obtener el objeto del estado
    state = state.get("State", state_id)

    # Verificar si el state existe
    if not state:
        abort(404)

    # Obtener lista de cities del state devolviendolas en json
    cities = [city.to_dict() for city in state.cities]

     # Devolver las ciudades como JSON
    return jsonify(cities)


@app_views_route('/api/v1/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city():
    cities = storage.get("City", city_id)

    # Verificar si el objeto city existe
    if city:

    # Convertir el objeto City devolviendolas en json
        return jsonify(city.to_dict())
    else:
        # Si el objeto City no existe, generar un error 404
        abort(404)
