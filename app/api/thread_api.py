# api/thread_api.py

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.thread_service import ThreadService

thread_api_blueprint = Blueprint('thread_api', __name__)
api = Api(thread_api_blueprint)

class ThreadResource(Resource):
    def get(self, thread_id):
        thread = ThreadService.get_thread_by_id(thread_id)
        if thread:
            return jsonify(thread.serialize())
        return {'message': 'Thread not found'}, 404

    def put(self, thread_id):
        data = request.get_json()
        thread = ThreadService.update_thread(thread_id, **data)
        if thread:
            return jsonify(thread.serialize())
        return {'message': 'Thread not found'}, 404

    def delete(self, thread_id):
        if ThreadService.delete_thread(thread_id):
            return {'message': 'Thread deleted'}, 200
        return {'message': 'Thread not found'}, 404

class ThreadListResource(Resource):
    def get(self):
        threads = ThreadService.get_all_threads()
        return jsonify([thread.serialize() for thread in threads])

    def post(self):
        data = request.get_json()
        thread = ThreadService.create_thread(**data)
        return jsonify(thread.serialize())

class ThreadByStageAndProjectResource(Resource):
    def get(self, stage_id, project_id):
        thread = ThreadService.get_thread_by_stage_and_project(stage_id, project_id)
        if thread:
            return jsonify(thread.serialize())
        return {'message': 'Thread not found for stage_id and project_id'}, 404

api.add_resource(ThreadByStageAndProjectResource, '/threads/<int:project_id>/<int:stage_id>')
api.add_resource(ThreadResource, '/threads/<int:thread_id>')
api.add_resource(ThreadListResource, '/threads')