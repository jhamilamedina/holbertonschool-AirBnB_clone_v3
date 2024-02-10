#!/usr/bin/python3

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/views')

<<<<<<< HEAD

from api.v1.views.states import *
from api.v1.views.cities import *
=======
if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
>>>>>>> cbf6111e91ae74ce415f60de768d3e0d49c12771
