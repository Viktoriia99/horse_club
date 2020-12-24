# from flask import jsonify, request, abort, make_response, url_for
# from app.models.to_do import ToDo
# from app.models.Plan import Plan
# from app.models.HorseStable import HorseStable
# from app.models.Role import Role
# from app.models.Owner import Owner
# from app.models.Horse import Horse
# from app.models.StableOccupancy import StableOccupancy
# from app.models.Discipline import Discipline
# from app.models.Subscription import Subscription
# from app.models.Client import Client
# from app.models.Trainer import Trainer
# from app.models.ClientSubscription import ClientSubscription
# from app.models.Schedule import Schedule
# from app.models.Photo import Photo
# from app import app, db
# from flask_httpauth import HTTPBasicAuth
#
# auth = HTTPBasicAuth()
#
# BASE_URL = '/todo/api/v1.0/tasks'
#
#
# @auth.verify_password
# def verify_password(email, password):
#     user = db.session.query(Client).filter(Client.email == email).first()
#     if user and user.check_password(password):
#         return email
#     return None
#
#
# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 401)
#
#
# # pereimenui
# @app.errorhandler(404)
# def not_found(error):
#     #or render_template("404.html")
#     return make_response(jsonify({'error': 'Not found'}), 404)
#
#
# def parse_task_to_json(task):
#     return {
#         'id': task.id,
#         'name': task.name,
#         'user_id': task.user_id,
#         'created_at': task.created_at,
#         'updated_on': task.updated_on,
#     }
#
#
# def make_public_task(task):
#     task = parse_task_to_json(task)
#     new_task = {}
#     for field in task:
#         if field == 'id':
#             new_task['url'] = url_for('get_task', task_id=task['id'], external=True)
#         else:
#             new_task[field] = task[field]
#     return new_task
#
#
# @app.route(BASE_URL, methods=['GET'])
# # @auth.login_required
# def get_tasks():
#     tasks = ToDo.query.all()
#     results = []
#
#     for to_do in tasks:
#         results.append(make_public_task(to_do))
#     response = jsonify({'tasks': results})
#     response.status_code = 200
#     return response
#
#
# @app.route(BASE_URL + '/<int:task_id>', methods=['GET'])
# # @auth.login_required
# def get_task(task_id):
#     task = ToDo.query.get(task_id)
#
#     if not task:
#         abort(404)
#
#     return jsonify({'task': parse_task_to_json(task)})
#
#
# @app.route(BASE_URL, methods=['POST'])
# @auth.login_required
# def create_task():
#     if not request.json or not 'name' in request.json:
#         abort(404)
#     dict_body = request.get_json()
#     task = Todo(name=dict_body['name'])
#
#     db.session.add(task)
#     db.session.commit()
#     return jsonify({'message': 'Now task successfully created.', 'task': parse_task_to_json(task)}), 201
#
#
# @app.route(BASE_URL + '/<int:task_id>', methods=['PUT'])
# @auth.login_required
# def updte_task(task_id):
#     task = Todo.query.get(task_id)
#     if not task:
#         abort(404)
#     if not request.json or not 'name' in request.json:
#         abort(404)
#
#     task.name = request.json.get('name', task.name)
#
#     db.session.add(task)
#     db.session.commit()
#     return jsonify({'task': parse_task_to_json(task)})
#
#
# @app.route(BASE_URL + '/<int:task_id>', methods=['DELETE'])
# @auth.login_required
# def delete_task(task_id):
#     task = ToDo.query.get(task_id)
#     if not task:
#         abort(404)
#
#     db.session.delete(task)
#     db.session.commit()
#     return jsonify({'result': True})
