from flask import Blueprint, jsonify, request, g
from models.song import Song, SongSchema, Comment, CommentSchema
from lib.secure_route import secure_route

api = Blueprint('songs', __name__)
song_schema = SongSchema()
comment_schema = CommentSchema()

@api.route('/songs', methods=['GET'])
def index():
    songs = Song.query.all()
    return song_schema.jsonify(songs, many=True), 200

@api.route('/songs/<int:song_id>', methods=['GET'])
def show(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'not found'}), 404
    return song_schema.jsonify(song), 200


@api.route('/songs/<int:song_id>/comments', methods=['POST'])
@secure_route
def comment_create(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Not Found'}), 404
    data = request.get_json()
    comment, errors = comment_schema.load(data)
    if errors:
        return jsonify(errors), 422
    comment.creator = g.current_user
    comment.song = song
    comment.save()
    return comment_schema.jsonify(comment), 202

@api.route('/songs/<int:song_id>/comments/<int:comment_id>', methods=['DELETE'])
@secure_route
def comment_delete(**kwargs):
    comment = Comment.query.get(kwargs['comment_id'])
    if comment.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'})
    if not comment:
        return jsonify({'message': 'Not Found'}), 404
    comment.remove()
    return '', 204
