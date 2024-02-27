# stage_api.py

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.stage_service import StageService

stage_api_blueprint = Blueprint('stage_api', __name__)
api = Api(stage_api_blueprint)

class StageResource(Resource):
    def get(self, stage_id):
        stage = StageService.get_stage_by_id(stage_id)
        if stage:
            return jsonify(stage.serialize())
        return {'message': 'Stage not found'}, 404

    def put(self, stage_id):
        data = request.get_json()
        stage = StageService.update_stage(stage_id, **data)
        if stage:
            return jsonify(stage.serialize())
        return {'message': 'Stage not found'}, 404

    def delete(self, stage_id):
        if StageService.delete_stage(stage_id):
            return {'message': 'Stage deleted'}, 200
        return {'message': 'Stage not found'}, 404

class StageListResource(Resource):
    def get(self):
        stages = StageService.get_all_stages()
        return jsonify([stage.serialize() for stage in stages])

    def post(self):
        data = request.get_json()
        stage = StageService.create_stage(**data)
        print(stage);
        return jsonify(stage.serialize())
        

api.add_resource(StageResource, '/stages/<int:stage_id>')
api.add_resource(StageListResource, '/stages')