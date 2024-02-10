#!/usr/bin/python3
"""Nuestra primera respuesta"""

from flask import jsonify
from api.v1.views import app_views
from console import classes
from models import storage
from models.base_model import BaseModel


@app_views.route('/status', strict_slashes=False)
def status():
    """Nuestra primera salida exitosa con un JSON"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def some_stats():
    """Cuenta todas las clases por tipo."""
    todos = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)