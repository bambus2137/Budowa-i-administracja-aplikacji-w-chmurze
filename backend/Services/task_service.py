from Repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def get_tasks():
        return TaskRepository.get_all()

    @staticmethod
    def get_task(task_id):
        return TaskRepository.get_by_id(task_id)

    @staticmethod
    def create_task(data):
        return TaskRepository.create(data)
