from flask import Blueprint, jsonify, request
from project.main.model.task import Task, TaskSchema
from project import db

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/task', methods=['POST'])
def add_task():
    request_content = request.json
    task = Task(content=request_content['content'])
    db.session.add(task)
    db.session.commit()

    task_schema = TaskSchema()
    task_dump = task_schema.dump(task)
    return jsonify(task_dump), 201

@task_routes.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    return '', 204
