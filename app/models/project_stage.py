
from app import db

class ProjectStage(db.Model):
    __tablename__ = 'project_stages'

    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), primary_key=True)
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.stage_id'), primary_key=True)
    assistant_id = db.Column(db.String(50), nullable=True)
    stage_description = db.Column(db.Text, nullable=True)

    def serialize(self):
        return {
            "project_id": self.project_id,
            "stage_id": self.stage_id,
            "assistant_id": self.assistant_id,
            "stage_description": self.stage_description
        }
    
    def __init__(self, project_id, stage_id, assistant_id=None, stage_description=None):
        self.project_id = project_id
        self.stage_id = stage_id
        self.assistant_id = assistant_id
        self.stage_description = stage_description

    def __repr__(self):
        return f"<ProjectStage project_id={self.project_id}, stage_id={self.stage_id}>"