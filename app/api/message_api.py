# message_api.py

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.message_service import MessageService

message_api_blueprint = Blueprint('message_api', __name__)
api = Api(message_api_blueprint)

class MessageResource(Resource):
    def get(self, message_id):
        message = MessageService.get_message_by_id(message_id)
        if message:
            return jsonify(message.serialize())
        return {'message': 'Message not found'}, 404

    def put(self, message_id):
        data = request.get_json()
        message = MessageService.update_message(message_id, **data)
        if message:
            return jsonify(message.serialize())
        return {'message': 'Message not found'}, 404

    def delete(self, message_id):
        if MessageService.delete_message(message_id):
            return {'message': 'Message deleted'}, 200
        return {'message': 'Message not found'}, 404

class MessageListResource(Resource):
    def get(self):
        messages = MessageService.get_all_messages()
        return jsonify([message.serialize() for message in messages])
        
    def post(self):
        data = request.get_json()
        message = MessageService.create_message(**data)
        return jsonify(message.serialize()), 201

api.add_resource(MessageResource, '/messages/<int:message_id>')
api.add_resource(MessageListResource, '/messages')