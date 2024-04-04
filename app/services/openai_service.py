from openai import OpenAI
from app import db
from app.models.message import Message
from app.models.thread import Thread
from datetime import datetime
import os
from dotenv import load_dotenv
import time
import json

def show_json(obj):
    print(json.loads(obj.model_dump_json()))

load_dotenv()
api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)


assistant_instructions = {}

def retrieve_instructions(ass_id):
    # if ass_id in assistant_instructions:
    #     return assistant_instructions[ass_id]
    # else:
        assistant = client.beta.assistants.retrieve(ass_id)
        instructions = assistant.instructions
        # Almacenar las instrucciones en el diccionario para futuros usos
        # assistant_instructions[ass_id] = instructions
        return instructions


def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


class OpenAIService:
    @staticmethod
    def send_to_openai_and_save(thread_id, message, ass_id, sender):
        db_thread = Thread.query.get(thread_id)
        print(db_thread)
        if not db_thread:
            return None
        openai_thread_id = db_thread.assistant_thread_id
        print("openai_thread_id_________",openai_thread_id)
        instruc = retrieve_instructions(ass_id)
        newMessage = client.beta.threads.messages.create(
            thread_id=openai_thread_id,
            role="user",
            content=message
        )
        run = client.beta.threads.runs.create(
            thread_id=openai_thread_id,
            assistant_id=ass_id,
            instructions=instruc
        )
        print("run______________:")
        show_json(run)
        # message_openAI = wait_for_run_completion(thread_id=openai_thread_id, run_id=run.id)
        run = wait_on_run(run, openai_thread_id)
        print("show wait run______________:")
        show_json(run)
        messages = client.beta.threads.messages.list(thread_id=openai_thread_id)
        print("show messages______________:")
        show_json(messages)
        message_openAI = messages.data[0].content[0].text.value
        print("message_openAI__________:",message_openAI)
        userMessage = Message(thread_id=thread_id, message=message, sender=sender)
        response_message = Message(thread_id=thread_id, message=message_openAI, sender="assistant")
        db.session.add(userMessage)
        db.session.add(response_message)
        db.session.commit()
        return response_message

    @staticmethod
    def getAssistantsOpenai():
        assistants = client.beta.assistants.list()
        assistants_data = []
        for assistant in assistants.data:
            assistant_data = {
                "id": assistant.id,
                "name": assistant.name,
                "instructions": assistant.instructions,
                "model": assistant.model,
                "created_at": assistant.created_at
            }
            assistants_data.append(assistant_data)
        # print("assistant data en servicio openai", assistants_data)
        return assistants_data