# /services/project_stage_service.py

from app.models import ProjectStage
from app import db
from app.models import Project
from app.models import Stage

class ProjectStageService:
    @staticmethod
    def get_project_stage_by_ids(project_id, stage_id):
        return ProjectStage.query.get((project_id, stage_id))

    @staticmethod
    def update_project_stage(project_id, stage_id, assistant_id=None, stage_description=None):
        project_stage = ProjectStageService.get_project_stage_by_ids(project_id, stage_id)
        if project_stage:
            if assistant_id is not None:
                project_stage.assistant_id = assistant_id
            if stage_description is not None:
                project_stage.stage_description = stage_description
            db.session.commit()
        return project_stage

    @staticmethod
    def delete_project_stage(project_id, stage_id):
        project_stage = ProjectStageService.get_project_stage_by_ids(project_id, stage_id)
        if project_stage:
            db.session.delete(project_stage)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_stages_by_project_id(project_id):
        return ProjectStage.query.filter_by(project_id=project_id).all()
    
    @staticmethod
    def create_project_stage(project_id, stage_id, assistant_id=None, stage_description=None):

        if not Project.query.get(project_id):
            raise ValueError("Proyecto no encontrado")
        if not Stage.query.get(stage_id):
            raise ValueError("Etapa no encontrada")

        new_project_stage = ProjectStage(
            project_id=project_id,
            stage_id=stage_id,
            assistant_id=assistant_id,
            stage_description=stage_description
        )
        db.session.add(new_project_stage)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e  # Aquí podrías querer elevar una excepción más específica o manejarla de otra manera
        return new_project_stage
    