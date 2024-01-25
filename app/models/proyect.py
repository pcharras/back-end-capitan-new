from app import db
from datetime import date

class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False, default=date.today)

    def serialize(self):
        return {
            "id": self.project_id,
            "name": self.name,
            "description": self.description,
            "date": self.date.isoformat() if self.date else None
        }
    
    def __init__(self, name, description=None, date=None):
        self.name = name
        self.description = description
        self.date = date or date.today()

    def __repr__(self):
        return f"<Project {self.project_id}: {self.name}>"
