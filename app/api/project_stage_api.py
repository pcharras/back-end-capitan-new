# /api/project_stage_api.py

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.project_stage_service import ProjectStageService

project_stage_api_blueprint = Blueprint('project_stage_api', __name__)
api = Api(project_stage_api_blueprint)

class ProjectStageResource(Resource):
    def get(self, project_id, stage_id):
        project_stage = ProjectStageService.get_project_stage_by_ids(project_id, stage_id)
        if project_stage:
            return jsonify(project_stage.serialize())
        return {'message': 'ProjectStage not found'}, 404

    def put(self, project_id, stage_id):
        data = request.get_json()
        project_stage = ProjectStageService.update_project_stage(project_id, stage_id, **data)
        if project_stage:
            return jsonify(project_stage.serialize())
        return {'message': 'ProjectStage not found'}, 404

    def delete(self, project_id, stage_id):
        if ProjectStageService.delete_project_stage(project_id, stage_id):
            return {'message': 'ProjectStage deleted'}, 200
        return {'message': 'ProjectStage not found'}, 404

        
class ProjectStageListResource(Resource):
    def get(self, project_id):
        project_stages = ProjectStageService.get_stages_by_project_id(project_id)
        return jsonify([stage.serialize() for stage in project_stages])
    def post(self, project_id):
        data = request.get_json()
        if not data or 'stage_id' not in data:
            return {'message': 'Missing required parameters'}, 400
        try:
            project_stage = ProjectStageService.create_project_stage(project_id, **data)
            return jsonify(project_stage.serialize()), 201
        except Exception as e:
            return {'message': str(e)}, 500
        
api.add_resource(ProjectStageResource, '/projects/<int:project_id>/stages/<int:stage_id>')
api.add_resource(ProjectStageListResource, '/projects/<int:project_id>/stages')