"""
Views for the Api app
"""

# third-party imports
from flask_restful import Resource, reqparse

# local imports
from app.utils import response_json, make_request
from app import constants

from .models import Videodirectoy
from .schemas import video_schema



class ApiResource(Resource):
    """
    This class represents Api views
    """
    def get(self):
        query = Videodirectoy.query.all()  #pylint: disable=line-too-long
        data = video_schema.dump(query)
        print(data)
        if data:
            return response_json(True, data, None)
        else:
            return response_json(True, data, constants.TEXT_DOES_NOT_EXISTS)

