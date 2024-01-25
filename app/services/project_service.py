from app.models import Project
from app import db
from datetime import date

class ProjectService:
    @staticmethod
    def get_project_by_id(project_id):
        return Project.query.get(project_id)

    @staticmethod
    def create_project(name, description=None, project_date=None):
        new_project = Project(name=name, description=description, date=project_date or date.today())
        db.session.add(new_project)
        db.session.commit()
        return new_project

    @staticmethod
    def update_project(project_id, name=None, description=None, project_date=None):
        project = ProjectService.get_project_by_id(project_id)
        if project:
            if name:
                project.name = name
            if description is not None:
                project.description = description
            if project_date:
                project.date = project_date
            db.session.commit()
        return project

    @staticmethod
    def delete_project(project_id):
        project = ProjectService.get_project_by_id(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_projects():
        return Project.query.all()
