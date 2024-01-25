# services/thread_service.py

from app.models import Thread
from app import db

class ThreadService:
    @staticmethod
    def get_thread_by_id(thread_id):
        return Thread.query.get(thread_id)

    @staticmethod
    def create_thread(timestamp, stage_id, project_id,assistant_thread_id):
        new_thread = Thread(timestamp=timestamp, stage_id=stage_id, project_id=project_id,assistant_thread_id=assistant_thread_id)
        db.session.add(new_thread)
        db.session.commit()
        return new_thread

    @staticmethod
    def update_thread(thread_id, timestamp=None, stage_id=None, project_id=None,assistant_thread_id=None):
        thread = ThreadService.get_thread_by_id(thread_id)
        if thread:
            if timestamp:
                thread.timestamp = timestamp
            if stage_id:
                thread.stage_id = stage_id
            if project_id:
                thread.project_id = project_id
            if assistant_thread_id:
                thread.assistant_thread_id = assistant_thread_id
            db.session.commit()
        return thread

    @staticmethod
    def delete_thread(thread_id):
        thread = ThreadService.get_thread_by_id(thread_id)
        if thread:
            db.session.delete(thread)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_threads():
        return Thread.query.all()