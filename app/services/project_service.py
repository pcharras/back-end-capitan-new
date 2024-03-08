from app.models import Project
from app.models import ProjectStage
from app import db
from datetime import date
from app.models import User

class ProjectService:
    @staticmethod
    def get_project_by_id(project_id):
        return Project.query.get(project_id)

    @staticmethod
    # Aclaración: busca el usuario con el public Id
    def create_project(name, creator_id, description=None, project_date=None):
        new_project = Project(name=name, creator_id=creator_id, description=description, date=project_date or date.today())
    # Agregar el creador del proyecto
        if creator_id:
            creator = User.query.filter_by(public_id=creator_id).first()
            print(creator)
            if creator:
                new_project.creator_id = creator.id
                new_project.collaborators.append(creator)

                db.session.add(new_project)
                db.session.commit()

                print(new_project)
                return new_project
            else:
                # Manejar el caso donde no se encuentra el usuario
                print(f"No se encontró ningún usuario con el public_id '{creator_public_id}'")
                return None

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
            print(project)
        return project

    @staticmethod
    def delete_project(project_id):
        # Obtener el proyecto por su ID
        project = ProjectService.get_project_by_id(project_id)
    
        if project:
            try:
                # Obtener todas las etapas asociadas al proyecto
                stages = ProjectStage.query.filter_by(project_id=project_id).all()
                
                # Eliminar cada etapa asociada al proyecto
                for stage in stages:
                    db.session.delete(stage)
                
                # Eliminar el proyecto
                db.session.delete(project)
                
                # Confirmar los cambios en la base de datos
                db.session.commit()
                
                return True
            except Exception as e:
                # Revertir la transacción en caso de error
                db.session.rollback()
                print(f"Error al eliminar el proyecto: {e}")
                return False
        
        return False

    @staticmethod
    def get_all_projects():
        return Project.query.all()


    @staticmethod
    def find_projects_by_user(public_id):
            # Buscar el usuario por su public_id
        user = User.query.filter_by(public_id=public_id).first()
        print("user en el servicio",user)
        if user:
                # Buscar los proyectos del usuario
            projects = user.projects
            print("en el servicio",projects)
            return projects
        else:
                # Manejar el caso donde no se encuentra el usuario
            print(f"No se encontró ningún usuario con el public_id '{public_id}'")
            return None   
    @staticmethod
    def add_collaborator_to_project(project_id, user_id):
        project = Project.query.get(project_id)
        if project:
            # Buscar el usuario por su ID
            collaborator = User.query.filter_by(public_id=user_id).first()
            if collaborator:
                if collaborator in project.collaborators:
                    return False, "El usuario ya es colaborador del proyecto."
                project.collaborators.append(collaborator)
                db.session.commit()
                return True, "Colaborador agregado exitosamente al proyecto."
            else:
                return False, f"No se encontró ningún usuario con el public_id '{collaborator_id}'."
        else:
            return False, f"No se encontró ningún proyecto con el ID '{project_id}'."