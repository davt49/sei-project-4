from flask import Blueprint
from models.category import Category, CategorySchema

api = Blueprint('categories', __name__)
song_categories = CategorySchema()

@api.route('/categories', methods=['GET'])
def index():
    categories = Category.query.all()
    return song_categories.jsonify(categories, many=True), 200
