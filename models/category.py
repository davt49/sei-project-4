from marshmallow import fields
from app import db, ma
from .base import BaseModel, BaseSchema

class Category(db.Model, BaseModel):

    __tablename__ = 'categories'

    name = db.Column(db.String(40), unique=True, nullable=False)

class CategorySchema(ma.ModelSchema, BaseSchema):
    songs = fields.Nested('SongSchema', many=True, only=('title', 'id'))

    class Meta:
        model = Category
