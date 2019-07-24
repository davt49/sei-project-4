from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
# from .user import User

class Forumtopic(db.Model, BaseModel):

    __tablename__ = 'forumtopics'

    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1200), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_forumtopics')

class ForumtopicSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Forumtopic

    forumcomments = fields.Nested('ForumcommentSchema', many=True, exclude=('forumtopic', 'created_at', 'updated_at'))
    creator = fields.Nested('UserSchema', only=('id', 'username'))

class Forumcomment(db.Model, BaseModel):

    __tablename__ = 'forumcomments'

    content = db.Column(db.Text, nullable=False)
    forumtopic_id = db.Column(db.Integer, db.ForeignKey('forumtopics.id'))
    forumtopic = db.relationship('Forumtopic', backref='forumcomments')
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_forumcommments')

class ForumcommentSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Forumcomment

    creator = fields.Nested('UserSchema', only=('id', 'username'))
