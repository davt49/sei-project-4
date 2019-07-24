from flask import Blueprint, jsonify, request, g
from models.forumtopic import Forumtopic, ForumtopicSchema, Forumcomment, ForumcommentSchema
from lib.secure_route import secure_route

api = Blueprint('forumtopics', __name__)
forumtopic_schema = ForumtopicSchema()
forumcomment_schema = ForumcommentSchema()

@api.route('/forumtopics', methods=['GET'])
def index():
    forumtopics = Forumtopic.query.all()
    return forumtopic_schema.jsonify(forumtopics, many=True), 200

@api.route('/forumtopics/<int:forumtopic_id>', methods=['GET'])
def show(forumtopic_id):
    forumtopic = Forumtopic.query.get(forumtopic_id)
    if not forumtopic:
        return jsonify({'message': 'not found'}), 404
    return forumtopic_schema.jsonify(forumtopic), 200

@api.route('/forumtopics', methods=['POST'])
@secure_route
def create():
    data = request.get_json()
    forumtopic, errors = forumtopic_schema.load(data)
    if errors:
        return jsonify(errors), 422
    forumtopic.creator = g.current_user
    forumtopic.save()
    return forumtopic_schema.jsonify(forumtopic), 201

@api.route('/forumtopics/<int:forumtopic_id>', methods=['PUT'])
@secure_route
def update(forumtopic_id):
    forumtopic = Forumtopic.query.get(forumtopic_id)
    if not forumtopic:
        return jsonify({'message': 'Not Found'}), 404
    if forumtopic.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'})
    data = request.get_json()
    errors = {}
    forumtopic, errors = forumtopic_schema.load(data, instance=forumtopic, partial=True)
    if errors:
        return jsonify(errors), 422
    forumtopic.save()
    return forumtopic_schema.jsonify(forumtopic), 202

@api.route('/forumtopics/<int:forumtopic_id>', methods=['DELETE'])
@secure_route
def delete(forumtopic_id):
    forumtopic = Forumtopic.query.get(forumtopic_id)
    if not forumtopic:
        return jsonify({'message': 'Not Found'}), 404
    if forumtopic.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'})
    forumtopic.remove()
    return '', 204

@api.route('/forumtopics/<int:forumtopic_id>/forumcomments', methods=['POST'])
@secure_route
def forumcomment_create(forumtopic_id):
    forumtopic = Forumtopic.query.get(forumtopic_id)
    if not forumtopic:
        return jsonify({'message': 'Not Found'}), 404
    data = request.get_json()
    forumcomment, errors = forumcomment_schema.load(data)
    if errors:
        return jsonify(errors), 422
    forumcomment.forumtopic = forumtopic
    forumcomment.creator = g.current_user
    forumcomment.save()
    return forumcomment_schema.jsonify(forumcomment), 202

@api.route('/forumtopics/<int:forumtopic_id>/forumcomments/<int:forumcomment_id>', methods=['DELETE'])
@secure_route
def forumcomment_delete(**kwargs):
    forumcomment = Forumcomment.query.get(kwargs['forumcomment_id'])
    if not forumcomment:
        return jsonify({'message': 'Not Found'}), 404
    if forumcomment.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'})
    forumcomment.remove()
    return '', 204
