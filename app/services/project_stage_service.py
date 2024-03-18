# /services/project_stage_service.py

from app.models import ProjectStage
from app import db
from app.models import Project
from app.models import Stage
from app.services.thread_service import ThreadService
import os



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
    # Realiza la consulta para obtener los datos de las etapas relacionadas con el proyecto
        stages_with_data = db.session.query(ProjectStage, Stage)\
            .join(Stage, ProjectStage.stage_id == Stage.stage_id)\
            .filter(ProjectStage.project_id == project_id)\
            .all()

        # Lista para almacenar los datos de las etapas
        stages_data = []

        # Itera sobre los resultados de la consulta
        for project_stage, stage in stages_with_data:
            # Crea un diccionario con los datos de cada etapa y su información relacionada
            stage_data = {
                'stage_id': stage.stage_id,
                'name': stage.name,
                'description': stage.description,
                'assistant_id': project_stage.assistant_id,
                'stage_description': project_stage.stage_description
            }
            # Agrega el diccionario a la lista de datos de etapas
            stages_data.append(stage_data)

        # Devuelve la lista de datos de etapas
        return stages_data




    
    @staticmethod
    def create_project_stage(project_id, stage_id, assistant_id=None, stage_description=None):
        # Verifica si el proyecto y la etapa existen
        if not Project.query.get(project_id):
            raise ValueError("Proyecto no encontrado")
        if not Stage.query.get(stage_id):
            raise ValueError("Etapa no encontrada")

        # Crea un nuevo hilo de conversación
        # thread = ThreadService.create_openai_thread()
        # print(thread)
        # Crea un nuevo objeto ProjectStage con el asistente y el hilo de conversación
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
            raise e 
        # Devuelve el nuevo objeto ProjectStage creado
        print(new_project_stage,)
        return new_project_stage