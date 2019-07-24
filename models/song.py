from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .category import Category
from .user import User

song_categories = db.Table(
    'song_categories',
    db.Column('song_id', db.Integer, db.ForeignKey('songs.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
)

class Song(db.Model, BaseModel):

    __tablename__ = 'songs'


    title = db.Column(db.String(80), nullable=False, unique=True)
    album = db.Column(db.String(160), nullable=False)
    music = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    lyric = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    review_link = db.Column(db.String(500), nullable=False)
    external = db.Column(db.String(500), nullable=False)
    categories = db.relationship('Category', secondary=song_categories, backref='songs')

class SongSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Song

    comments = fields.Nested('CommentSchema', many=True, exclude=('song', 'created_at', 'updated_at'))
    categories = fields.Nested('CategorySchema', many=True, exclude=('created_at', 'updated_at', 'songs'))

class Comment(db.Model, BaseModel):

    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    song = db.relationship('Song', backref='comments')
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_commments')

class CommentSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Comment

    creator = fields.Nested('UserSchema', only=('id', 'username'))
