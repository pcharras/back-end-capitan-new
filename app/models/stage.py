# stage.py

from app import db

class Stage(db.Model):
    __tablename__ = 'stages'

    stage_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            "id": self.stage_id,
            "name": self.name,
            "description": self.description
        }

    def __init__(self,name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Stage {self.stage_id}: {self.name} - {self.description}>"