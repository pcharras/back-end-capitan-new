# models/thread.py

from app import db

class Thread(db.Model):
    __tablename__ = 'threads'

    thread_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.stage_id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), nullable=False)
    assistant_thread_id = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            "id": self.thread_id,
            "timestamp": self.timestamp.isoformat(),
            "stage_id": self.stage_id,
            "project_id": self.project_id,
            "assistant_thread_id":self.assistant_thread_id
        }
    
    def __repr__(self):
        return f"<Thread {self.thread_id}>"