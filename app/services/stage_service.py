# stage_service.py

from app.models import Stage
from app import db

class StageService:
    @staticmethod
    def get_stage_by_id(stage_id):
        return Stage.query.get(stage_id)

    @staticmethod
    def create_stage(name, description):
        print(description);
        new_stage = Stage(name=name, description=description)
        db.session.add(new_stage)
        db.session.commit()
        return new_stage

    @staticmethod
    def update_stage(stage_id, name=None, description=None):
        stage = StageService.get_stage_by_id(stage_id)
        if stage:
            if name is not None:
                stage.name = name
            if description is not None:
                stage.description = description
            db.session.commit()
        return stage

    @staticmethod
    def delete_stage(stage_id):
        stage = StageService.get_stage_by_id(stage_id)
        if stage:
            db.session.delete(stage)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_stages():
        return Stage.query.all()