# message_service.py

from app.models import Message
from app import db
from datetime import datetime

class MessageService:
    @staticmethod
    def get_message_by_id(message_id):
        return Message.query.get(message_id)

    @staticmethod
    def create_message(thread_id, message_text, message_timestamp=None, sender="user"):
        new_message = Message(thread_id=thread_id, message=message_text, timestamp=message_timestamp or datetime.now(),sender=sender)
        db.session.add(new_message)
        db.session.commit()
        return new_message

    @staticmethod
    def update_message(message_id, message_text=None, message_timestamp=None):
        message = MessageService.get_message_by_id(message_id)
        if message:
            if message_text:
                message.message = message_text
            if message_timestamp:
                message.timestamp = message_timestamp
            db.session.commit()
        return message

    @staticmethod
    def delete_message(message_id):
        message = MessageService.get_message_by_id(message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_messages():
        return Message.query.all()
#traer mensajes por hilo
    @staticmethod
    def get_messages_by_thread(thread_id):
        return Message.query.filter_by(thread_id=thread_id).all()    