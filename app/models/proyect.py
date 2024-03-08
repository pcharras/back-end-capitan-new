from app import db
from datetime import date

user_project_association = db.Table('user_project_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('projects.project_id'), primary_key=True)
)

class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False, default=date.today)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_projects', foreign_keys=[creator_id])
    collaborators = db.relationship('User', secondary=user_project_association, backref='projects')

    def serialize(self):
        return {
            "id": self.project_id,
            "name": self.name,
            "description": self.description,
            "date": self.date.isoformat() if self.date else None,
            "creator": self.creator_id if self.creator else None,
            "collaborators": [user.serialize() for user in self.collaborators]
        }
    
    def __init__(self, name, creator_id=None, description=None, date=None):
        self.name = name
        self.creator_id = creator_id
        self.description = description
        self.date = date or date.today()
        
    def __repr__(self):
        return f"<Project {self.project_id}: {self.name} by {self.creator_id}>"
