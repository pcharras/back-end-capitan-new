# services/thread_service.py
from datetime import date
from app.models import Thread
from app import db
from openai import OpenAI
import os
from dotenv import load_dotenv
from app.models import User
from app.services.message_service import MessageService

load_dotenv()
api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)


class ThreadService:
    @staticmethod
    def create_openai_thread():
        new_thread = client.beta.threads.create()
        return new_thread

    @staticmethod
    def delete_thread_openai(assistant_thread_id):
        deleted_thread = client.beta.threads.delete(assistant_thread_id)
        print("deleted thread", deleted_thread)
        return deleted_thread

    @staticmethod
    def get_thread_by_id(thread_id):
        thread = Thread.query.get(thread_id)
        return thread

    @staticmethod
    def create_thread( stage_id, project_id, user_public_id):
        user = User.query.filter_by(public_id=user_public_id).first()
        if user:
            user_id = user.id

        # Crear un hilo en OpenAI
            openai_thread = ThreadService.create_openai_thread()
            new_thread = Thread(stage_id=stage_id, project_id=project_id, assistant_thread_id= openai_thread.id, user_id=user_id, timestamp= date.today())
            db.session.add(new_thread)
            db.session.commit()
            return new_thread
        else:
            print(f"No se encontró ningún usuario con el public_id '{user_public_id}'")
            return None

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

    def delete_thread(thread_id):
        thread = ThreadService.get_thread_by_id(thread_id)
        print(thread)
        assistant_thread_id = thread.assistant_thread_id
        print(thread)
        if thread:
            MessageService.delete_messages_by_thread(thread_id)
            ThreadService.delete_thread_openai(assistant_thread_id)
            db.session.delete(thread)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_threads():
        return Thread.query.all()

    @staticmethod
    def get_thread_by_stage_and_project(stage_id, project_id):
        return Thread.query.filter_by(stage_id=stage_id, project_id=project_id).first()