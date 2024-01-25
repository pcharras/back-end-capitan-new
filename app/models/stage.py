# stage.py

from app import db

class Stage(db.Model):
    __tablename__ = 'stages'

    stage_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            "id": self.stage_id,
            "description": self.description
        }

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"<Stage {self.stage_id}: {self.description}>"