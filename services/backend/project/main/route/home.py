from flask import Blueprint, jsonify
from project.main.service import task_service

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def home():
    records = task_service.query_all()
    return jsonify(records)