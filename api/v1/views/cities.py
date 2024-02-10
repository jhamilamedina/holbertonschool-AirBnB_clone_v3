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
    if not city:
        abort(404)

    # Convertir el objeto City devolviendolas en json
    return jsonify(city.to_dict())


@app_views_route('/api/v1/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    # Obtener el objeto City
    city = storage.get("City", city_id)

    # Verificar si el objeto City existe
    if not city:
        abort(404)
    # Eliminar el objeto City
    storage.delete(city)
    storage.save()

    # Devolver un diccionario vacío con código de estado 200 (OK)
    return jsonify({}), 200


@app_views_route('/api/v1/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    # Verificar si el estado existe
    state = storage.get("State", state_id)
    if not state:
        abort(404)

    # Obtener el cuerpo JSON de la solicitud
    city_data = request.get_json()
    if not city_data:
        abort(400, "Not a JSON")

    # Verificar si el nombre de la ciudad está presente en el JSON
    if 'name' not in city_data:
        abort(400, "Missing name")

    # Creación de una nueva ciudad
    city_data['State'] = state_id
    new_city = City(**city_data)
    new_city.save()

    # Devolver la nueva ciudad con el código de estado 201 (Created)
    return jsonify(new_city.to_dict()), 201


@app_views_route('/api/v1/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def update_city(city_id):
    # Obtener el objeto City
    city = storage.get("City", city_id)

    # Verificar si el objeto City existe
    if not city:
        abort(404)

    # Verificar si el cuerpo de la solicitud HTTP es un JSON válido
    if not request.get_json:
        abort(400, "Not a JSON")

    # Obtener el diccionario del cuerpo de la solicitud HTTP
    data = request.get_json()

    # Verificar si el diccionario contiene la clave 'name'
    if 'name' not in data:
        abort(400, "Missing name")

    # Actualizar el objeto Ciudad con los datos del diccionario
    ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(city, key, value)

    # Guardar los cambios en la base de datos
    storage.save()

    # Devolver el objeto Ciudad actualizado con el código de estado 200
    return jsonify(city.to_dict()), 200
