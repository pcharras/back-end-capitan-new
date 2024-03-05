from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.project_service import ProjectService

project_api_blueprint = Blueprint('project_api', __name__)
api = Api(project_api_blueprint)

class ProjectResource(Resource):
    def get(self, project_id):
        project = ProjectService.get_project_by_id(project_id)
        if project:
            return jsonify(project.serialize())
        return {'message': 'Project not found'}, 404

    def put(self, project_id):
        data = request.get_json()
        project = ProjectService.update_project(project_id, **data)
        if project:
            return jsonify(project.serialize())
        return {'message': 'Project not found'}, 404

    def delete(self, project_id):
        if ProjectService.delete_project(project_id):
            return {'message': 'Project deleted'}, 200
        return {'message': 'Project not found'}, 404

class ProjectListResource(Resource):
    def get(self):
        projects = ProjectService.get_all_projects()
        return jsonify([project.serialize() for project in projects])
        
    def post(self):
        print (request.get_json())
        data = request.get_json()

        project = ProjectService.create_project(**data)
        if project:
            return jsonify(project.serialize())
        # return jsonify(project.serialize()), 201
    

class UserProjectsResource(Resource):
    def get(self, public_id):
        projects = ProjectService.find_projects_by_user(public_id)
        print("en la ruta",projects)
        if projects:
            return jsonify([project.serialize() for project in projects])
        return projects

api.add_resource(ProjectResource, '/projects/<int:project_id>')
api.add_resource(ProjectListResource, '/projects')
api.add_resource(UserProjectsResource, '/projects/user/<string:public_id>')
