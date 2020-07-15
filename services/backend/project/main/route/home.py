from flask import Blueprint, jsonify
from project.main.model.task import Task

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def hello_world():
    return jsonify(hello="world")