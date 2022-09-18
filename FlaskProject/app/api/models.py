"""
Models for the Api app
"""

# local imports
from app.db import db
import datetime


class Videodirectoy(db.Model):
    __tablename__ = 'video_directory'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    video_title = db.Column(db.String(120), unique=True)
    video_discription = db.Column(db.String(240))
    thumbnail_links = db.Column(db.String(240))
    published_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()