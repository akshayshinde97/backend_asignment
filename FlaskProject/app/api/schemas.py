"""
Schemas for the Api app
"""

# local imports
from app.db import marshmallow
from .models import Videodirectoy


class VideoSchema(marshmallow.Schema):
    class Meta:
        model = Videodirectoy
        load_instance = True


# pylint: disable=invalid-name
video_schema = VideoSchema()