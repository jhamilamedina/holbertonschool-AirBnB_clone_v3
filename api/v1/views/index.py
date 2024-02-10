#!/usr/bin/python3
"""Nuestra primera respuesta"""

from tkinter import Place
from flask import jsonify
from api.v1.views import app_views
from console import classes
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User


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