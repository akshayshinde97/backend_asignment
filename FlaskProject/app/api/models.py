"""
Models for the Api app
"""

# local imports
# from app.db import db
# import datetime

# # class Wallet(db.Model):
# #     """
# #     This class represents the videodirectory table.
# #     """
# #     __tablename__ = 'wallets'

# #     id = db.Column(db.Integer, primary_key=True)
# #     currency_code = db.Column(db.String(length=3))
# #     open_exchange_price = db.Column(db.Float(precision=8))
# #     requested_amount = db.Column(db.Float(precision=8))
# #     final_amount = db.Column(db.Float(precision=8))
# #     created_on = db.Column(db.DateTime, index=True, server_default=db.func.now())
# #     updated_on = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

# #     def __repr__(self):
# #         return '<id: {}>'.format(self.id)

# #     def save(self):
# #         db.session.add(self)
# #         db.session.commit()


# class Videodirectoy(db.Model):
#     __tablename__ = 'video_directory'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     video_title = db.Column(db.String(120), unique=True)
#     video_discription = db.Column(db.String(240))
#     thumbnail_links = db.Column(db.String(240))
#     published_at = db.Column(db.DateTime)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.now())

#     def save(self):
#         db.session.add(self)
#         db.session.commit()