"""SQLalchemy models and utility functions for assignment"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter user table that will correspond to tweets - SQLAlchemy syntax"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    name = DB.Column(DB.String, nullable=False) # represents a twitter user name

    def __repr__(self):
        return "<User: {}>".format(self.name)

class Tweet(DB.Model):
    """Tweet text data - associated with Users Table"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column temporary key
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False) # linking to the User class
    user = DB.relationship("User", backref=DB.backref('tweets', lazy=True)) # essentially joining the User and Tweet table

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)