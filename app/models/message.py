# message.py

from app import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('threads.thread_id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now)
    sender = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "message_id": self.message_id,
            "thread_id": self.thread_id,
            "message": self.message,
            "timestamp": self.timestamp.isoformat(),
            "sender": self.sender
        }
    
    def __init__(self, thread_id, message, sender, timestamp=None):
        self.thread_id = thread_id
        self.message = message
        self.sender = sender
        self.timestamp = timestamp or datetime.now()

    def __repr__(self):
        return f"<Message {self.message_id}: {self.message}>"