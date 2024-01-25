# message.py

from app import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('threads.thread_id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now)

    def serialize(self):
        return {
            "message_id": self.message_id,
            "thread_id": self.thread_id,
            "message": self.message,
            "timestamp": self.timestamp.isoformat()
        }
    
    def __init__(self, thread_id, message, timestamp=None):
        self.thread_id = thread_id
        self.message = message
        self.timestamp = timestamp or datetime.now()

    def __repr__(self):
        return f"<Message {self.message_id}: {self.message}>"